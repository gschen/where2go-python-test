import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#tensorflow 2.0 学习笔记
#基础操作篇
import tensorflow as tf
import numpy as np
'''
1.TF中的数据表达
    Tf.Tensor
    what's Tensor
        标量    scalar : 1.1    
        向量    vector : [1.1],[1.1,2.2,...]
        矩阵    matrix : [[0.7,1.5],[2.1,3],[5,6]]
        维度大于2的矩阵    tensor : rank>2
    从工程上来讲所有数据都可以叫做tensor,tensor是tensorflow上数据的载体
2.TF中的数据类型
    int,float,double
    bool
    string
'''
'''
page_1
创建一个常量or创建一个tensor
'''
a=tf.constant(1)#默认为32位
b=tf.constant(2.,dtype=tf.double)#创建浮点型tensor，并指定为双精度
c=tf.constant([True,False])#创建布尔型
d=tf.constant('hello,word')#创建字符串型
'''
tensor常用属性
'''
#指定tensor在哪个设备上运行，gpu or cpu
with tf.device("cpu"):
    a=tf.constant([1])
with tf.device('gpu'):
    b=tf.range(4)
#查看tensor在哪个设备上运行
a.device
#因为我使用的是cpu版本的tensorflow，所以只能在cpu上运行
b.device
#tensor的运行设备转移
aa=a.gpu()
bb=b.cpu()
#将tensor转换成numpy
b.numpy()
#查看维度
b.ndim#返回维度
tf.rank(b)#或者这个，还能查看shape和dtype
b.shape()#与python中的shape功能相似

#判断某个数据是不是tensor,下面两种方式
isinstance(a,tf.Tensor)
tf.is_tensor(b)
#查看数据类型
a.dtype,b.dtype
#判断数据类型
a.dtype=tf.float32
#数据类型转换
a=np.arange(5)#numpy生成的数据都默认为64位
aa=tf.convert_to_tensor(a)#转换为tensor
aa=tf.convert_to_tensor(a,dtype=tf.int32)#转换为tensor，并改为32位
tf.cast(aa,dtype=tf.float32)#将aa转换为浮点型32位
b=tf.constant([0,1])
tf.cast(b,dtype=tf.bool)#整型0、1可以和布尔类型相互转换

#Variable 变量，可更改优化的数据.在tensorflow中Variable自带可求导特性
a=tf.range(5)
b=tf.Variable(a)

#isinstance存在一些问题，一般建议用tf.is_tensor
isinstance(b,tf.Tensor)#False
tf.is_tensor(b)#True

#返回tensor中的具体数据
a.numpy()

#创建tensor
'''
    1.form numpy,list   从numpy和python的list中经转换得到
    2.zeros,ones        np.zeros、np.ones，tf.zeros、tf.ones
    3.fill              随意用某个数填充
    4.random            随机化的初始化
    5.constant          
    6.Application       
'''
#直接用List,要求list中的数据都可以转换为可计算的数据
tf.convert_to_tensor([1,2])
tf.convert_to_tensor([[1],[2.0]])

#ones,zeros接受的数据是shape，[2,3]指生成二行三列的矩阵
tf.convert_to_tensor(np.ones[2,3])
tf.convert_to_tensor(np.zeros[2,3])
#与上方功能相同
tf.ones([2,3])
tf.zeros([2,3])

tf.zeros_like(a)#生成与a的shape相同的全0矩阵
#等同于
tf.zeros(a.shape)

tf.fill([2,2],9)#生成2行2列的tensor，并用9填充

#正态分布初始化
tf.random.normal([2,2],mean=1,stddey=1)#生成2行2列的tensor，其中的每个值都通过正态分布得出
#mean是均值、stddey是方差。不填默认0、1，标准正态分布

#截断正态分布,去除正态分布中左右两侧较少的分布区域值，一般来说比直接的正态分布好
tf.random.truncated_normal([2,2],mean=0,stddey=1)

#均匀分布
tf.random.uniform([2,2],minval=0,maxval=1)#从0到1之间均匀采样

#随机打散，假设现在a中有48张照片，28*28，3通道的，用tensor表示为[48,28,28,3]
#现在要将这些照片顺序打散
index=tf.range(48)#生成对应索引，每个索引对应一张照片
idx=tf.random.shuffle(index)#将index随机打乱，但是图片的顺序还没发生变化
a=tf.gather(a,index)#用gather函数可以让照片与被打乱的index一一对应，这样就实现了随机打散




