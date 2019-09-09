import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 2 * x + 1
y2 = x ** 2

plt.xlim((-1, 1))
plt.ylim((-2, 4))
plt.xlabel("X")
plt.ylabel("Y")

l1 = plt.plot(x, y, color='red', linewidth=1.0, linestyle='--', label='up')
l2 = plt.plot(x, y2, label='down')

# 打印图例(plot中label标签的值)
# plt.legend()
# 可以用loc参数指定图例的位置
# plt.legend(loc='best')
# 可以用labels指定label的名字，若在此处指定则plot中label的指定无效
plt.legend(labels=['first', 'second'], loc='best')

plt.show()
