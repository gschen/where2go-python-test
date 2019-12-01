"""
使用pip命令安装NumPy后做如下操作，
"""
import numpy as np
"""引入numpy库"""
new_numpy=(np.arange(1,13).reshape(4,3))              #求数组
print(new_numpy)

numpy_ndim = new_numpy.ndim                              #求维数
print(numpy_ndim)

numpy_shape = new_numpy.shape                            #矩阵规模（x,y）为x*y
print(numpy_shape)

numpy_size = new_numpy.size                              #矩阵元素个数（numpy_shape之积）
print(numpy_size)

"""矩阵的创建"""

numpy_one = np.array([1,2,3])       #创建矩阵
print(numpy_one)

numpy_two = np.zeros((3,4))         #创建元素全为0的矩阵
print(numpy_two)

numpy_three = np.ones((3,3))        #创建元素全为1的矩阵
print(numpy_three)

numpy_four = np.arange(1,13)        #创建范围矩阵
print(numpy_four)

"""矩阵的运算"""
numpy_1 = np.array([1,2,3,4])
numpy_2 = np.array([5,6,7,8])

numpy_sum = numpy_1 + numpy_2             #求和
print(numpy_sum)

numpy_cha = numpy_2 - numpy_1
print(numpy_cha)                           #求差

numpy_ji = numpy_2 * 2
print(numpy_ji)                            #求积