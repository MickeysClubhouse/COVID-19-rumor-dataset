import powerlaw
from matplotlib.pyplot import figure
from matplotlib import rc
import pylab
from numpy import genfromtxt
from matplotlib.font_manager import FontProperties

pylab.rcParams['xtick.major.pad'] = '8'
pylab.rcParams['ytick.major.pad'] = '8'
# pylab.rcParams['font.sans-serif']='Arial'

rc('font', family='sans-serif')
rc('font', size=10.0)
rc('text', usetex=False)

panel_label_font = FontProperties().copy()
panel_label_font.set_weight("bold")
panel_label_font.set_size(12.0)
panel_label_font.set_family("sans-serif")

blackouts = genfromtxt('input/news_count.txt')

data = blackouts  # / 10 ** 3  # data can be list or numpy array
results = powerlaw.Fit(data)
print("alpha", results.power_law.alpha)
print("sigma", results.power_law.sigma)
R, p = results.distribution_compare('power_law', 'exponential',normalized_ratio=True)
print("R:", R)
print("p:", p)

# get the fit range
# fit = powerlaw.Fit(data) 6.1
# print("xmin:", fit.xmin)
# print("alpha:", fit.alpha)
# print("D:", fit.D)
fit = powerlaw.Fit(data, xmin=6.0)
print("xmin:", fit.xmin)
print("fixed_min", fit.fixed_xmin)
print("alpha:", fit.alpha)
print("D:", fit.D)


def plot_basics(data, data_inst, fig, units):
    from powerlaw import plot_pdf, Fit, pdf
    annotate_coord = (-.1, .95)
    # annotate_coord = (1.1, .95)

    ax1 = fig.add_subplot(n_graphs, n_data, data_inst)
    x, y = pdf(data, linear_bins=True)
    ind = y > 0
    y = y[ind]
    x = x[:-1]
    x = x[ind]
    ax1.scatter(x, y, color='r', s=.5)
    plot_pdf(data[data > 0], ax=ax1, color='b', linewidth=2)
    from pylab import setp
    setp(ax1.get_xticklabels(), visible=True)

    # ABC
    # if data_inst == 1:
    ax1.annotate("A", annotate_coord, xycoords="axes fraction", fontproperties=panel_label_font)
    ax1.set_ylabel(u"p(X)")
    from mpl_toolkits.axes_grid.inset_locator import inset_axes
    ax1in = inset_axes(ax1, width="30%", height="30%", loc=3)
    ax1in.hist(data, density=True, color='b')
    ax1in.set_xticks([])
    ax1in.set_yticks([])
    ax1.set_xlabel(units)

    ax2 = fig.add_subplot(n_graphs, n_data, n_data + data_inst, sharex=ax1)
    plot_pdf(data, ax=ax2, color='b', linewidth=2, label="pdf of data")
    fit = Fit(data, xmin=1, discrete=True)
    fit.power_law.plot_pdf(ax=ax2, linestyle=':', color='g', label="power law fit")
    p = fit.power_law.pdf()

    ax2.set_xlim(ax1.get_xlim())

    fit = Fit(data, discrete=True)
    fit.power_law.plot_pdf(ax=ax2, linestyle='--', color='g', label="power law fit--opt xmin")
    from pylab import setp
    setp(ax2.get_xticklabels(), visible=True)

    # if data_inst == 1:
    ax2.annotate("B", annotate_coord, xycoords="axes fraction", fontproperties=panel_label_font)
    ax2.set_ylabel(u"p(X)")  # (10^n)")
    handles, labels = ax2.get_legend_handles_labels()
    ax2.legend(handles, labels, loc=3)
    ax2.set_xlabel(units)

    ax3 = fig.add_subplot(n_graphs, n_data, n_data * 2 + data_inst)  # , sharex=ax1)#, sharey=ax2)
    fit.power_law.plot_pdf(ax=ax3, linestyle='--', color='g', label="power law fit from opt-min")
    fit.exponential.plot_pdf(ax=ax3, linestyle='--', color='r', label="exponential fit from opt-min")

    fit.plot_pdf(ax=ax3, color='b', linewidth=2, label="pdf from opt-min")

    ax3.set_ylim(ax2.get_ylim())
    ax3.set_xlim(ax1.get_xlim())
    handles, labels = ax3.get_legend_handles_labels()
    ax3.legend(handles, labels, loc=3)
    ax3.set_xlabel(units)

    # if data_inst == 1:
    ax3.annotate("C", annotate_coord, xycoords="axes fraction", fontproperties=panel_label_font)
    ax3.set_ylabel(u"p(X)")
    ax3.set_xlabel(units)


n_data = 3
n_graphs = 4
# f = figure(figsize=(8, 11))
f = figure(figsize=(16, 22))

data_inst = 3
units = "Times that the Rumors\nare Reported Online"
plot_basics(data, data_inst, f, units)

# save the figure
f.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=.3, hspace=.2)
figname = 'FigNews'
f.savefig(figname + '.eps', bbox_inches='tight')
# f.savefig(figname+'.tiff', bbox_inches='tight', dpi=300)
