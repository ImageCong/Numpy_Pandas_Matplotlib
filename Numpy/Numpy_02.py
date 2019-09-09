import numpy as np

# 可以使用dtype指定矩阵中的元素的类型（int32 int64 float等）
array = np.array([[1, 23, 4]], dtype=np.int64)
print(array.dtype)

# zeros(x,y)方法生成x行y列的空矩阵
array2 = np.zeros((3, 4))
print(array2)

# ones(x,y)生成x行y列的值为1的矩阵
array3 = np.ones((2, 5))
print(array3)

array4 = np.empty((3, 4))
print(array4)

# 生成一个矩阵，元素为从10到20步长为2的数
array5 = np.arange(10, 20, 2)
print(array5)

# 只填写一个参数默认为第二个参数，即最大元素为11
array6 = np.arange(12)
print(array6)

# 通过reshape()方法产生x行y列的矩阵
array7 = np.arange(12).reshape((3, 4))
print(array7)

# linspace()生成线段，每段间隔一致
# 代码含义为从1到10生成5个等分的线段（可以reshape）
array8 = np.linspace(1, 10, 5)
print(array8)
