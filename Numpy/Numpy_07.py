import numpy as np

A = np.arange(12).reshape(3, 4)
print(A)
'''
 0  1  2  3
 4  5  6  7
 8  9  10 11
'''
# 横向分割
print(np.split(A, 3, axis=0))
print(np.vsplit(A, 3))
# 纵向分割
print(np.split(A, 4, axis=1))
# 纵向分割，每组两列
print(np.hsplit(A, 2))

# 不等分割
# 第一组分了前两列，第二、三组各一列
print(np.array_split(A, 3, axis=1))

