import matplotlib.pyplot as plt
import numpy as np

'''
    plot是画一条线
    scatter是画散点图
'''

x = np.linspace(-2, 2, 50)
y = 2 * x + 1
y2 = x ** 2

plt.xlim((-2, 2))
plt.ylim((-2, 4))

plt.xlabel("X")
plt.ylabel("Y")

# 替换坐标轴的坐标值
ticks = np.linspace(-2, 2, 9)
print(ticks)
plt.xticks(ticks)

plt.yticks([-2, -1, 0, 1, 2, 4], ['really bad', 'bad', 'normale', 'fine', 'good', 'excellent'])

plt.plot(x, y, color='red', linewidth=1.0, linestyle='--')
plt.plot(x, y2)

# 取得坐标轴
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

x0 = 1
y0 = 2 * x0 + 1
# 使用scatter画点，这里只画一个点
# s代表size
plt.scatter(x0, y0, s=50, color='b')
# k代表black
# --代表'--'类型的虚线
# lw代表线的宽度
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)

# Annotation标注
# r代表row string $...$之间是美化的字体
# %s后跟的%y0代表将y0赋值给s
# xy=(指定点的坐标)
# xycoords='data'代表xy中传的是坐标值而非其他
# xytext与textcoords联系
# textcoords='offset points'是指将我们给定的坐标作为基准，根据xytext中的参数进行偏移
# fontsize代表字的大小
# arrowprops 设置一个箭头，需要传入一个字典类型的参数
#            其中arrowstyle设置箭头形式，connectionstyle设置弧长、曲率
plt.annotate(r"$2x+1=%s$" % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30), textcoords='offset points',
             fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))

# Annotation标注的另一种使用方法
plt.text(-1.5, 3, r'This is an annotation', fontdict={'size': 18, 'color': 'red'})

plt.show()
