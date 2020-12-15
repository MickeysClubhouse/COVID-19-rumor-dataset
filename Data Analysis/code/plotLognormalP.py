import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.font_manager import FontProperties

# todo: change file name of the source data
#file_name = "input/twitter_lognormal.txt"
file_name = "input/news_lognormal.txt"
dataset = []
y1 = []
file = open(file_name, mode='r')
for line in file:
    dataset = line.split()
file.close()
for data in dataset:
    y1.append((int(data)) / 100)
print(y1)

rc('font', family='sans-serif')
rc('font', size=15.0)
rc('text', usetex=False)

panel_label_font = FontProperties().copy()
panel_label_font.set_weight("bold")
panel_label_font.set_size(30.0)
panel_label_font.set_family("sans-serif")

f = plt.figure(figsize=(8, 4))  # 设置画布的尺寸
#plt.title('Goodness-of-fit on Twitter data (lognormal)', fontsize=20)
plt.title('Goodness-of-fit on News data (lognormal)', fontsize=20)   # todo: title and font size
plt.xlabel(u'Size of simulated data', fontsize=20)  # 设置x轴，并设定字号大小
plt.xlim(2000, 31000)
plt.ylabel(u'$p_{ks}$', fontsize=20)  # 设置y轴，并设定字号大小
plt.ylim(0, 1)
annotate_coord = (-.15, 1.05)
x1 = [3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000,
      20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000, 30000]  # todo: change this part to fit the data set

ax=plt.plot(x1, y1, label='average p changes', linewidth=3, color='r', marker='.',
         markerfacecolor='blue', markersize=20)
plt.annotate("c", annotate_coord, xycoords="axes fraction", fontproperties=panel_label_font)
plt.legend(loc=2)  # 图例展示位置，数字代表第几象限
plt.show()  # 显示图像

#figname = 'twitter lognormal result'
figname='news lognormal result'  # todo: change figure name
f.savefig(figname + '.eps', bbox_inches='tight')  # if don't have Photoshop, please save as .tiff
