#神经网络与全连接

#数据集加载
import tensorflow as tf
'''
1.小型常用经典数据集加载
    keras.datasets
    tf.data.Dataset.from_tensor_slices
        shuffle
        map
        batch
        repeat

    we will talk INPUT Pipeline later

'''

'''
tf.keras
keras.datasets
    boston housing
        Boston housing price regression dataset
        波士顿房价制定因子作为输入，比如地段，收入等等
    mnist/fashion mnist
        MNIST/Fashion-MNIST dataset
        手写数字识别
    cifar10/100
        small images classification dataset
        图片分类
    imdb
        sentiment classification dataset
        类似于淘宝评论之类的，有好坏分类，根据评论分析评论好坏
'''
#案例：手写数字集加载   numpy格式
(x,y),(x_test,y_test)=tf.keras.datasets.mnist.load_data()
x.shape#[60000,28,28]60k张照片，28*28大小
y.shape#[60000]#60k张图的对应lable,0-9
x_test.shape#[10000,28,28]
y_test.shape#[10000]
x.min()#0
x.max()#255
y_onehot=tf.one_hot(y,depth=10)#转换为one_hot编码


#CIFAR10/100   numpy格式
# CIFAR10指数据集里的图片分类有10类
#CIFAR100指数据集里有10个大类，每个大类里又有10个小类
#每张图片的shape[32,32,3]
(x,y),(x_test,y_test)=tf.keras.datasets.cifar10.load_data()
x.shape#[50000,32,32,3]
y.shape#[50000,1]
x_test.shape#[10000,32,32,3]
y_test.shape#[10000,1]10k张图的对应lable

#tf.data.Dataset()
#将numpy转换为tensor并将图片迭代

db=tf.data.Dataset.from_tensor_slices(x_test)
next(iter(db))
#iter是迭代器，next(iter(db))每次返回集里的一张图片
db=tf.data.Dataset.from_tensor_slices((x_test,y_test))
#一次迭代两个集，（image,lable）
next(iter(db))[0]
#[0]是image,[1]是该次迭代的image对应的label

db=db.shuffle(10000)
#打乱前10000张图片和对应的lable，但每张图片对应的并不会乱

#数据预处理,tensor默认是64位，需要转换为32位
#这里的x是具体的某张图片,y是对应的lable
def preprocess(x,y):
    x=tf.cast(x,dtype=tf.float32)/255
    y=tf.cast(y,dtype=tf.int32)
    y=tf.one_hot(y,depth=10)
    return x,y
db2=db.map(preprocess)
res=next(iter(db2))#迭代

#batch
db3=db2.batch(32)#以32张图片为一组,[32,32,32,3]
res=next(iter(db3))
res[0].shape#[32,32,32,3]
res[1].shape#[32,1,10]，# 这个1没用，是最开始的[50000,1]里的那个里，
# 所以没用的维度要在做预处理的时候就要去掉


db4=db3.repeat(2)#不填，默认无限次
for x,y in db4:#由于上行代码，整个for循环会执行2次
    pass

