import numpy as np

array = np.arange(2, 14).reshape(3, 4)
print(array)

# 输出的是最小/最大值的索引（下标）
print(" 最小值索引：", np.argmin(array))
print(" 最大值索引：", np.argmax(array))
# 求平均值
print(" 平均值：", np.mean(array))
print(" 平均值：", np.average(array))
# 求中位数
print(" 中位数：", np.median(array))
# 累加，当前位置和之前所有位置累加的和
print("各位置累加：", np.cumsum(array))
# 累差，下一位置和当前位置的差(n个数有n-1个差)
print("各位置累差：", np.diff(array))
# 输出非零的数，按照(x行),(y列)的输出
print("非零：", np.nonzero(array))
# 逐行排序
print("逐行排序：", np.sort(array))
# 矩阵转置
# (A.T).dot(B) 可以将A的转置与B做矩阵乘法
print("矩阵转置：\n", array.T)
# 保留x y之间的数，这里的x=5,y=9
# 小于5的数全部变为5，大于9的数全部变为9
print("保留x,y之间的数：\n", np.clip(array, 5, 9))
