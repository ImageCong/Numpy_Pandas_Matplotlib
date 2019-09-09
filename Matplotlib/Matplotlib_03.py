import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 2 * x + 1
y2 = x ** 2

plt.xlim((-1, 1))
plt.ylim((-2, 4))

plt.xlabel("X")
plt.ylabel("Y")

# 替换坐标轴的坐标值
ticks = np.linspace(-1, 1, 5)
print(ticks)
plt.xticks(ticks)

plt.yticks([-2, -1, 0, 1, 2, 4], ['really bad', 'bad', 'normale', 'fine', 'good', 'excellent'])

plt.plot(x, y, color='red', linewidth=1.0, linestyle='--')
plt.plot(x, y2)

# 取得坐标轴
ax = plt.gca()
# 取消上方和右侧的坐标轴
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# 设置x轴在上方，y轴在右侧
# ax.xaxis.set_ticks_position('top')
# ax.yaxis.set_ticks_position('right')

# 下面两个设置完后坐标原点为(0,0)
# 设置下方坐标轴位置为0
ax.spines['bottom'].set_position(('data', 0))
# 设置左侧坐标轴位置为0
ax.spines['left'].set_position(('data', 0))



plt.show()
