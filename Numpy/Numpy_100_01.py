# 1、使用np导入numpy的包
import numpy as np
import warnings

warnings.filterwarnings("ignore")

# 2、打印numpy的版本号和配置信息
print(np.__version__)
np.show_config()

# 3、创建向量空间，尺寸为10
arr = np.arange(10)
print(arr)

# 4、查出数组占用内存的体积
Z = np.zeros((10, 10))
print("%d bytes" % (Z.size * Z.itemsize))

# 5、使用命令行来获得numpy中add这个函数的文档
# python -c "import numpy;numpy.info(numpy.add)"

# 6、创建一个大小为10的空向量，但第五个值为1
Z = np.zeros(10)
Z[4] = 1
print(Z)

# 7、创建一个值为从10到49的向量[10,11,12...49]
Z = np.arange(10, 50, 1)
print(Z)

# 8、反转一个向量（第一个元素变为最后一个）
Z = Z[::-1]
print(Z)

# 9、创建一个3x3矩阵，其值范围为0到8
Z = np.arange(9).reshape(3, 3)
print(Z)

# 10、从[1,2,0,0,4,0]中查找出所有非零元素
Z = np.nonzero([1, 2, 0, 0, 4, 0])
print(Z)

# 11、创建一个 3 * 3单位矩阵
Z = np.eye(3)
print(Z)

# 12、使用随机值创建一个 $333$ 数组
Z = np.random.random((3, 3, 3))
print(Z)

# 13、使用随机值创建一个10x10数组，并找出其最小值和最大值
Z = np.random.random((10, 10))
max = Z.max()
min = Z.min()
print("max: ", max, "   min: ", min)

# 14、创建一个大小为30的随机向量并找到平均值
Z = np.arange(30)
ave = Z.mean()
print("average: ", ave)

# 15、创建一个2维数组，边框元素都为1，内部元素都为0
Z = np.ones((5, 5))
Z[1:-1, 1:-1] = 0
print(Z)

# 16、如何在一个既有数组周围添加边框（用0填充）
Z = np.ones((5, 5))
Z = np.pad(Z, pad_width=1, mode="constant", constant_values=0)
print(Z)

# 17、
'''
0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
np.nan in set([np.nan])
0.3 == 3 * 0.1
表达式结果是什么？

答：
nan
False
False
nan
True
False
'''
# 18、创建一个5x5矩阵, 其对角线下方的数值正好是1,2,3,4
Z = np.zeros((5, 5))
for i in range(1, Z.__len__()):
    Z[i][i - 1] = i
print(Z)

Z = np.diag(1 + np.arange(4), k=-1)
print(Z)

# 19、创建一个8x8矩阵并用棋盘图案填充它
Z = np.zeros((8, 8), dtype=int)
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
print(Z)

# 20、假设有一个（6,7,8）形状的三维数组，那么其中第100个元素的索引（x，y，z）是什么
print(np.unravel_index(100, (6, 7, 8)))

# 21、使用tile函数创建棋盘格8x8矩阵
Z = np.zeros((2, 2))
Z = np.tile(Z, (4, 4))
print(Z)

# 22、把一个5x5随机矩阵归一化
Z = np.random.random((5, 5))
Z = (Z - np.mean(Z)) / (np.std(Z))
print(Z)

# 23、创建一个自定义dtype，用这个数据类型可以将颜色描述为四个无符号字节    RGBA
color = np.dtype([("r", np.ubyte, 1),
                  ("g", np.ubyte, 1),
                  ("b", np.ubyte, 1),
                  ("a", np.ubyte, 1)])
print(color)

# 24、5x3矩阵乘以3x2矩阵（实矩阵乘积）
Z = np.dot(np.ones((5, 3)), np.arange(6).reshape((3, 2)))
print(Z)

# 25、给定一维数组，所有在3到8之间的元素都变成其负数(正->负, 负->正).
Z = np.arange(11)
Z[(3 <= Z) & (8 >= Z)] *= -1
print(Z)

# 26、这段脚本的输出是什么
'''
print(sum(range(5),-1))
答：
10 
因为range(5)是1-5，每个加-1就是0-4
0-4求和为10
'''

# 27、设有整数向量Z，这些表达式中的哪些是合法的
'''
Z**Z
2 << Z >> 2  只有这个不合法
Z <- Z
1j*Z
Z/1/1
Z<Z>Z
'''

# 28、以下表达式的结果是什么
'''
np.array(0) / np.array(0)
np.array(0) // np.array(0)
np.array([np.nan]).astype(int).astype(float)

答：
nan
0
[-2.14748365e+09]
'''

# 29、如何让一个浮点类型数组里面的值全部取整?

# uniform(下限，上限，输出样本数)
Z = np.random.uniform(-10, +10, 10)
# copysign(A,B) 把B的符号给A
# ceil(num) 计算大于等于num的最小整数
print(np.copysign(np.ceil(np.abs(Z)), Z))

# 30、如何在两个数组之间找到相同的值
Z1 = np.random.randint(0, 10, 10)
print(Z1)
Z2 = np.random.randint(0, 10, 10)
print(Z2)
print(np.intersect1d(Z1, Z2))
