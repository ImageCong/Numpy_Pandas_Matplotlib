import pandas as pd
import numpy as np

# # 合并数据
# # 方法1
# df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
# df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
# df3 = pd.DataFrame(np.ones([3, 4]) * 2, columns=['a', 'b', 'c', 'd'])
#
# print(df1)
# print(df2)
# print(df3)
#
# # ignore_index可以让之前的index不被考虑，避免重复
# res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
# print(res)
#
# print("......................................................")

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
print(df1)
print(df2)

# 默认为外连接
res = pd.concat([df1, df2], sort='False')
print(res)
# 指定内连接
res = pd.concat([df1, df2], join='inner', sort='False')
print(res)

# 按列进行合并
res = pd.concat([df1, df2], axis=1, ignore_index=True)
print(res)

# append添加，默认向下添加，可以指定axis=1横向添加
# 也可以添加多个，只要用列表就行
res = df1.append(df2, ignore_index=True, sort=False)
print(res)

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
res = df1.append(s1, ignore_index=True)
print(res)



# test
d1 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
d2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'])
print(d1)
print(d2)
re = d1.append(d2, sort=False, ignore_index=True)
print(re)
re = pd.concat([d1, d2], ignore_index=True, sort=False)
print(re)
re = pd.concat([d1, d2], ignore_index=True, sort=False, join='inner')
print(re)
