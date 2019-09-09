import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.arange(5)
print(a)
print(b)
print(b < 3)
print(b ** 2)

c = a - b
print("a-b")
print(c)

d = 10 * np.sin(a)
print("10*sin(a)")
print(d)
print()

# *和dot的区别
# dot运算进行的是矩阵乘法，而普通的乘号是相应位置做乘法
arr = np.array([[1, 1], [0, 1]])
brr = np.arange(4).reshape(2, 2)

# 乘法运算
r1 = arr * brr
# dot运算 两种方式均可
r2 = np.dot(arr, brr)
r3 = arr.dot(brr)
print("乘法运算")
print(r1)
print("dot运算")
print(r2)
print(r3)

# 随机生成2行4列矩阵
a = np.random.random((2, 4))
print(a)
print(np.max(a))
print()
# axis=0为每一列求 axis=1为每一行求
print(np.max(a, axis=0))
print(np.max(a, axis=1))
