import pandas as pd
import numpy as np
# 处理丢失数据
dates = pd.date_range('20190906', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)

df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan

print(df)
# 删除丢失数据NaN的行
print(df.dropna(axis=0, how='any'))
# 删除丢失数据NaN的列
print(df.dropna(axis=1, how='any'))
# 当how='all'的时候 数据行/列全为NaN才丢弃
df.iloc[1: 2] = np.nan
print(df)
print(df.dropna(axis=0, how='all'))

# 把NaN填为0
print(df.fillna(value=0))
# 判断是否缺失
print(df.isnull())
# 当表格很大不好找的时候可以采取如下的判断
print(np.any(df.isnull()) == True)
