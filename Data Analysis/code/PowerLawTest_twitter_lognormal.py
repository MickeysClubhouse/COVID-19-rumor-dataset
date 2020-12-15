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
panel_label_font.set_size(20.0)
panel_label_font.set_family("sans-serif")

blackouts = genfromtxt('input/tweets.txt')

data = blackouts  # / 10 ** 3  # data can be list or numpy array
results = powerlaw.Fit(data)
print("alpha", results.power_law.alpha)
print("sigma", results.power_law.sigma)
R, p = results.distribution_compare('power_law', 'lognormal',  normalized_ratio=True)
print(R)
print(p)


def plot_basics(data, data_inst, fig, units):
    from powerlaw import plot_pdf, Fit, pdf
    annotate_coord = (-.3, .95)
    # annotate_coord = (1.1, .95)
    fit = powerlaw.Fit(data, discrete=True)
    ####
    fit.distribution_compare('power_law', 'lognormal')
    fig = fit.plot_ccdf(linewidth=3, label='Empirical Data')
    fig.annotate("b", annotate_coord, xycoords="axes fraction", fontproperties=panel_label_font)
    fit.power_law.plot_ccdf(ax=fig, linewidth=2, color='r', linestyle='--', label='Power law fit:\n$x_{min}=661.0$,$α=1.494$')
    fit.lognormal.plot_ccdf(ax=fig,  linewidth=2,  color='g', linestyle='--', label='Lognormal fit:\n$p_{ks} ∈ [0.2,0.4]$,\n$x_{min}=661.0$,$σ=0.019$')
    ####
    fig.set_ylabel(u"p(X≥x)", fontsize=18)
    fig.set_xlabel(units, fontsize=18)
    handles, labels = fig.get_legend_handles_labels()
    fig.legend(handles, labels, loc=3, fontsize=15)


n_data = 3
n_graphs = 4
f = figure(figsize=(5, 6))

data_inst = 3
units = ' Popularity (X) of rumors\nin Twitter dataset'
plot_basics(data, data_inst, f, units)

# save the figure
f.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=.3, hspace=.2)
figname = 'FigTwitter_Lognormal'
f.savefig(figname + '.eps', bbox_inches='tight')
# f.savefig(figname+'.tiff', bbox_inches='tight', dpi=300)
