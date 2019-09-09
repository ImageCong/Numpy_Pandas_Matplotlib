import numpy as np

array = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6)
print(array)

b = np.arange(0, 60, 10).reshape(-1, 1)

print(np.equal(array, b))
print(np.less(b,array))

