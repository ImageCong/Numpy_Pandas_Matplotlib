import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 50)
y = 2 * x + 1

plt.xlim((-2, 2))
plt.ylim((-2, 4))

plt.xlabel("X")
plt.ylabel("Y")

# 替换坐标轴的坐标值
ticks = np.linspace(-2, 2, 9)
print(ticks)
plt.xticks(ticks)

plt.yticks([-2, -1, 0, 1, 2, 4], ['really bad', 'bad', 'normale', 'fine', 'good', 'excellent'])

plt.plot(x, y, color='red', linewidth=8.0)

# 取得坐标轴
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
# ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# 获得x轴y轴的全部坐标值
# 设置他们的字号为14
# set_bbox为设置label后面的background的相关属性
# facecolor为背景色，edgecolor为边框色，alpha为不透明度
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(14)
    label.set_bbox(dict(facecolor='orange', edgecolor='None', alpha=0.5))

plt.show()
