import pandas as pd
import numpy as np

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2'],
                     }, index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                      'D': ['D0', 'D1', 'D2'],
                      }, index=['K0', 'K2', 'K3'])
# merge合并
print(left)
print(right)
# 默认按照inner的方式进行合并
res = pd.merge(left, right, left_index=True, right_index=True)
print(res)
# 设定outer
res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
print(res)

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']
                     })
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3'],
                      })
print(left)
print(right)
# 按照key合并
res = pd.merge(left, right, on='key')
print(res)

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']
                     })
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3'],
                      })
print(left)
print(right)
# on后面也可以跟多个参数，用列表。按照两个key合并
# 默认inner的连接方式
res = pd.merge(left, right, on=['key1', 'key2'])
print(res)
# 指定outer
res = pd.merge(left, right, on=['key1', 'key2'], how='outer')
print(res)
