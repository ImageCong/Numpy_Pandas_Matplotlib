import pandas as pd
import numpy as np

# pandas更像一个字典
s = pd.Series([1, 3, 5, np.nan, 44, 1])
print(s)

dates = pd.date_range('20190905', periods=6)
print(dates)
print()

# 默认DataFrame格式
df2 = pd.DataFrame(np.random.rand(6, 4))
print(df2)
# 指定行/列名
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)
print("df.index: \n", df.index)
print("df.columns: \n", df.columns)
print()

# 对数字进行描述
# 包括求和、平均、最大、最小等等
print(df2.describe())
print()

# 排序
# axis=0 指定列排序
# ascending=False指定降序
print(df.sort_index(axis=0, ascending=False))
# 根据value排序
# by='a'指定根据'a'列排序
print(df.sort_values(by='a'))
