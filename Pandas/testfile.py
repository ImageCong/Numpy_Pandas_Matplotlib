import pandas as pd
import numpy as np

data = pd.read_excel(r"data2.xlsx", encoding='utf-8')
print(data)

print(data["时间"][0])

data["时间"] = data["时间"].astype("int64")

start = np.array(data.head(1).iloc[:, :1])
end = np.array(data.tail(1).iloc[:, :1])

# 这里的diff是转为了一个list
diff = end[0] - start[0]
# 这里才变为数值
diff = diff[0] / 1000 / 1000 / 1000
print(diff)

index = data.shape[0] - 1


print("缺失的数据条数为：", int(diff - index), "条")
