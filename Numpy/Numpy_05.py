import numpy as np

A = np.arange(3, 15)

print(A)
print(A[3])

A = A.reshape(3, 4)
print(A, "\n")
print(A[2])
# 1行1列
print(A[1][1])
print(A[1, 1])
# 2行所有
print(A[2:])
# 1列所有
print(A[:, 1])

# 返回一个一行的序列
print(A.flatten())
# 由此我们可以用flat来访问矩阵中的每个元素
for item in A.flat:
    print(item, end=" ")
