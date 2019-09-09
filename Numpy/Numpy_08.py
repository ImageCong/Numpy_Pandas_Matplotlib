import numpy as np

a = np.arange(4)
print(a)

b = a
c = a
d = b
print(b)
print(c)
print(d)
# 由此可见 b=a这类操作实际上是引用
# 二者指向同一块内存
a[0] = 11
print(a)
print(b)
print(c)
print(d)
a[0] = 0

# 使用copy不产生关联
# 只拷贝外部元素，共享内部嵌套元素
b = a.copy()
c = a[:]
a[0] = 1
print("a\n", a)
print("b:\n", b)
print("c:\n", c)

print(id(a))
print(id(b))
print(id(c))
