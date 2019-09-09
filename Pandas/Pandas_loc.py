import pandas as pd

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': ['2000', '2001', '2002', '2001', '2002'],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                     index=['one', 'two', 'three', 'four', 'five'])
print(frame)

'''
    按行索引
    loc和iloc
        loc是根据index来索引
        iloc是根据行号索引
'''
print(frame.loc[['one', 'two']])
print(frame.iloc[:3])

# 按列索引
print(frame[['year', 'pop']])
