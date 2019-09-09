import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Pandas画图
# 默认index=np.arange(num)
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
# 把生成的数据累加
data = data.cumsum()

# 本来用plt.plot(x=,y=)
# 但是data本身即是数据，直接plot即可
data.plot()

# 生成图像
plt.show()

data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))
print(data.head())
data = data.cumsum()
data.plot()
plt.show()

ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label='Class 1')
data.plot.scatter(x='A', y='C', c='DarkGreen', label='Class 2', ax=ax)
data.plot.scatter(x='A', y='D', color='Yellow', label='Class 3', ax=ax)
plt.show()
