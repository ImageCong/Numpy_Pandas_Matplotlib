import matplotlib.pyplot as plt
import numpy as np

n = 12

X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

# 生成柱状图
plt.bar(X, +Y1)
plt.bar(X, -Y2)

# x,y+0.05都是偏移量，打印的annotation是'%.2f' % y
# 实际上打印的是保留2位小数的y
for x, y in zip(X, Y1):
    plt.text(x, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y1):
    plt.text(x, -y - 0.05, '-%.2f' % y, ha='center', va='bottom')

plt.xlim(-0.5, n)
plt.ylim(-1.25, 1.25)
plt.xticks(())
plt.yticks(())

plt.show()
