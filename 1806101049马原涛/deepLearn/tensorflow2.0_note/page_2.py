#索引与切片1
import tensorflow as tf
import numpy1 as np

#1.与python列表相同取法
a=tf.ones([1,5,5,3])#一个tensor，5行5列3通道
a[0][0]#取a中的第一个tensor的第一行
a[0][0][0]#取a中的第一个tensor的第一行第一列
a[0][0][0][2]#取a中的第一个tensor的第一行第一列的第三个值

#2.numpy风格取法
a=tf.random.normal([4,28,28,3])
a[1].shape#返回TensorShape([28,28,3])
a[1,2].shape#返回TensorShape([28,3])
a[1,2,3].shape#返回TensorShape([3])
a[1,2,3,2].shape#返回TensorShape([]),标量、shape为空

#3.切片索引
a=tf.range(10)#[0,1,2,3,4,5,6,7,8,9]
a[-1:]#[9]
a[-2:]#[8,9]
a[:2]#[0,1]
a[:-1]#取完
#a[-1]返回的是标量9，a[-1:]返回的是向量[9]

#4.
a=tf.random.normal(4,28,28,3)
a[:,:,:,2]#取所有照片中所有像素点的第三个通道值
a[:,0,:,:]#取所有照片中第一行的所有像素点的三通道值

#5.跨步采样  a[start:end:step] a[起点：终点：步长]
a=tf.range(10)#[0,1,2,3,4,5,6,7,8,9]
a[::2]#返回0,2,4,6,8
a=tf.random.normal(4,28,28,3)
a[:,:14:2,:14:2,:]#取所有照片的1到14行和列步长为2

#6.逆序采样
a=tf.range(4)#[0,1,2,3]
a[::-1]#[3,2,1,0]
#a[A:B:-X]A>B,从A到B按步长x采样，包括A。A<B,从B到A按步长x采样,不包括B。
a[2::-2]#返回[2,0]

#7.省略号...
a=tf.random.normal([4,28,28,3])
a[0,...]#取第1张照片的所有值
a[...,0]#取所有照片的第一个通道值
a[0,...,2]#取第一张照片的第三个通道值
#...放在左右两侧或者中间某个地方，一般应用于维度较多的情况

#8.无规律采样
'''
[4,28,28,3]采取第二个维度也就是a[1]的时候。第二个维度表示28行。
假设第一次采第3行，第二次采第27行，第三次采第9行，第四次采第3行。如何做呢？
indices[3,27,9,13]
Selective Indexing  
    tf.gather
    tf.gather_nd
    tf.boolean_mask
'''
'''
    假设有一组数据data=[classes,students,subjects]=[4,35,8]
    表示4个班级，35个学生，8门科目
    
'''

#tf.gather
data=tf.random.normal([4,35,8])
tf.gather(data,axis=0,indices=[2,3])
#axis表示取哪一个维度，indices表示取该维度的哪些值
#此处表示取班级中的第3、4个班级
#等同于data[2:4]

tf.gather(data,axis=0,indices=[2,1,3,0])
#先收第3个班级、再收第二个2班级、再收第4个班级、再收第1个班级的信息

tf.gather(data,axis=1,indices=[2,6,8,7,15])
#表示从每个班抽取五位同学，每个班抽取的同学序号都是2,6,8,7,15

#tf.gather_nd 表示同时对多维度进行操作，例下
tf.gather_nd(data,[0])#取第1个班级，a.shape为[35,8]
tf.gather_nd(data,[0,1])#取第一个班级的第二个同学的所有科目成绩
tf.gather_nd(data,[0,1,4])#取第一个班级的第二个同学的第5门课的成绩

#


