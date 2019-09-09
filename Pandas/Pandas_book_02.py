import pandas as pd
import numpy as np

'''
    DataFrame
        表格型数据结构
        同时具有行索引、列索引
        含有一组有序的列，每列可以是不同类型
        
        column和index都可以有名称
        
'''
# df = pd.DataFrame(np.arange(12).reshape(3, 4), columns=['A', 'B', 'C', 'D'], index=[1, 2, 3])
# print(df)
#
# print(df[:-1])

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': ['2000', '2001', '2002', '2001', '2002'],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                     index=['one', 'two', 'three', 'four', 'five'])
print(frame)

frame['debt'] = np.arange(5)
print(frame)

frame['debt'] = pd.Series([13, 15, 17], index=['two', 'three', 'five'])
print(frame)

# 当state时Ohio时 输出True
# 同时为frame创建了一个新列
frame['estate'] = frame.state == 'Ohio'
print(frame)

# DataFrame与嵌套字典
# 外层字典的键作为列，内层字典的键作为行索引
dic = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 2.3, 2002: 3.7}}
frame2 = pd.DataFrame(dic)
print(frame2)
print(frame2.reindex(['2000', '2001', '2002']))
