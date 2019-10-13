#维度变换
import tensorflow as tf
import numpy as np
#View
'''
    [b,28,28]=[照片数、行、列]
    [b,28*28]=[照片数、照片信息] #不关注图片的二维信息
    [b,2b14*28]=[照片数、将图片分为上下两部分、照片信息]
    [b,28,28,3]=[照片数、行、列、通道数]


'''
a=tf.random.normal([4,28,28,3])
tf.reshape(a,[4,784,3])
tf.reshape(a,[4,-1,3])#与上行含义相等

tf.reshape(a,[4,784*3])
tf.reshape(a,[4,-1])#与上行含义相等

tf.reshape(a,[4,18,38,3])#保证整体信息不变，既可以随意变换

'''
    [4,28,28,3]变换为[4,784,3]
    要变回来需要记住原图片信息height和width
    height维度在前width维度在后
'''
#[b,h,w,c]的内部变换
#如[h,w]要变为[w,h]，需要用到矩阵的转置
a=tf.random.normal((4,3,2,1))
#交换3和2的位置，也可以理解为交换h和w的顺序
tf.transpose(a,perm=[0,2,1,3])#返回[4,2,3,1]

tf.transpose(a)#返回[1,2,3,4]

#pytocth中的[b,c,h,w]，如果在tensorflow中用到这些数据就需要进行变换转换为[b,h,w,c]

#维度的增加和减少
#expand
#a[classes,students,classes]
a=tf.random.normal([4,35,8])
tf.expand_dims(a,axis=0)#返回[1,4,35,8]
#axis为正，在对应下标的维度前边添加
#axis为负,在对应下标的维度后边添加

#squeeze 维度减少，用于减少shape为1的维度
a=tf.random.normal([1,4,35,8])#去掉shape为1的维度
tf.squeeze(a)#自动去掉shape为1的维度
tf.squeeze(a,axis=0)#去掉第一个维度
