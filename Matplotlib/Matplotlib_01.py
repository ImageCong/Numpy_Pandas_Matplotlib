import matplotlib.pyplot as plt
import numpy as np

'''
    figure
        在不同的figure中可以放不同的图片
        每次用plt.figure()后
        就会创建一个新的figure
        在下一个figure之前全部都是这个figure的设定
'''

# 生成-1到1的50个点
x = np.linspace(-1, 1, 50)
y = 2 * x + 1
y2 = x ** 2

plt.figure()
plt.plot(x, y)
plt.show()
# figsize=(长，宽)
plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y2)
plt.plot(x, y, color='red', linewidth=1.0, linestyle='--')
plt.show()
