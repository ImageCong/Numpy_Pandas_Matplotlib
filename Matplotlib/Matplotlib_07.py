import matplotlib.pyplot as plt
import numpy as np

n = 1024
# normal(0,1,n)代表平均值为0，方差为1,生成n个数
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
# 为了颜色好看,取消以后只有一个颜色
T = np.arctan2(Y, X)

plt.scatter(X, Y, s=75, c=T, alpha=0.5)

plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))

plt.show()
