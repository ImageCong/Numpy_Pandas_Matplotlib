import pandas as pd
import numpy as np

dates = pd.date_range('20190906', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])

print(df)
print("`````````````````````````````````````````````````")

# 下面那两种方式都一样，代表选择column为A的那一列
print(df['A'])
print(df.A)
print("`````````````````````````````````````````````````")

# 切片选择
print(df[0:3])
print(df['20190906':'20190908'])
print("`````````````````````````````````````````````````")
# 以标签的方式选择
# 通过行、列名选择
print(df.loc['20190907'])
print(df.loc['20190907', ['A', 'B']])

# 按位置选择
# 通过索引选择
# index为第三行第一列
print(df.iloc[3, 1])

# bool筛选
# 筛选出A列小于8的数据
print(df[df.A < 8])
