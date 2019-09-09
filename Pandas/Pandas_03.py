import pandas as pd
import numpy as np

dates = pd.date_range('20190906', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)

# pandas更改值
df.iloc[2, 2] = 1111
print(df)
df.loc['20190907', 'D'] = 0
print(df)

# 增加新的一列
df['E'] = pd.Series(['1', '2', '3', '4', '5', '6'], index=dates)
print(df)
