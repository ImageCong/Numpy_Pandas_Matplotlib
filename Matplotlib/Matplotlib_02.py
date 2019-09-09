import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 2 * x + 1
y2 = x ** 2

# 设置坐标轴
plt.xlim((-1, 1))
plt.ylim((-2, 4))
# 设置坐标轴标签
plt.xlabel("X")
plt.ylabel("Y")

# 替换坐标轴的坐标值
ticks = np.linspace(-1, 1, 5)
print(ticks)
# 此处仅更换了x轴的
plt.xticks(ticks)
# 将坐标值替换为文字
# 可以用$转字体，空格需要用\转义
# r""代表正则
plt.yticks([-2, -1, 0, 1, 2, 4], ['really bad', 'bad', 'normale', 'fine', r'$good$', r'$excellent$'])

plt.plot(x, y, color='red', linewidth=1.0, linestyle='--')
plt.plot(x, y2)
plt.show()
