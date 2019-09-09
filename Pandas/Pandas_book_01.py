import pandas as pd

'''
    Series
        类似于一维数组的对象
        由一组数据以及一组与之相关的索引构成
        索引在左、值在右
        
        可以被看作一个字典，可以被用到需要用到字典的函数中
        也可以直接用字典创建Series
        
        Series最重要的功能:
            算数运算中自动对齐到不同索引的数据
'''
ser = pd.Series([4, 5, 6, 2, 1])
print(ser)
print(ser.values)
print(ser.index)

