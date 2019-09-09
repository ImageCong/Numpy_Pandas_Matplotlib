import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

# vstack的参数是一个Tuple
# 功能为将元素内的矩阵合并
C = np.vstack((A, B, [3, 3, 3]))

print("A为(x行，y列)： ", A.shape)
print("C为(x行，y列)： ", C.shape)

print("C矩阵为:\n", C)

'''
    使用转置T不能把一个单行序列转为单独的一列
    即，假设A=[1,1,1]，A.T仍然为[1,1,1]
'''
# 解决办法：
# 1、使用A[:, np.newaxis]来改变A的维度
# 2、使用reshape(-1,1)
print(A[:, np.newaxis])
print(A.reshape(-1, 1))
print()

A = np.array([1, 1, 1])[:, np.newaxis]
B = np.array([2, 2, 2])[:, np.newaxis]
# 横向合并ABBA四个（A、B此处为列向量）
# 不指定axis=1默认为纵向合并
C = np.concatenate((A, B, B, A), axis=1)
print(C)
