#实战
#forward前向传播(张量)
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets
#x:[60k,28,28]
#y:[60k}
(x,y),_=datasets.mnist.load_data()
#转换为tensor
x = tf.convert_to_tensor(x,dtype=tf.float32)/255
#x范围由0-255变为0-1
y = tf.convert_to_tensor(y,dtype=tf.int32)
'''
print(x.shape,y.shape,x.dtype,y.dtype)
print(tf.reduce_min(x),tf.reduce_max(x))
print(tf.reduce_min(y),tf.reduce_max(y))
'''
train_db=tf.data.Dataset.from_tensor_slices((x,y)).batch(128)
train_iter=iter(train_db)
sample=next(train_iter)
print("batch：",sample[0].shape,sample[1].shape)

#[b,784]->[b,256]->[b,128]->[b,10]
w1 = tf.Variable(tf.random.truncated_normal([784,256],stddev=0.1))
b1=tf.Variable(tf.zeros([256]))
w2 = tf.Variable(tf.random.truncated_normal([256,128],stddev=0.1))
b2=tf.Variable(tf.zeros([128]))
w3 = tf.Variable(tf.random.truncated_normal([128,10],stddev=0.1))
b3=tf.Variable(tf.zeros([10]))
lr=1e-3
for epoch in range(10):
    for step,(x,y) in enumerate(train_db):
        #x:[128,28,28]
        #y:[128]
        #[b,28,28]->[b,28*28]
        x=tf.reshape(x,[-1,28*28 ])

        with tf.GradientTape() as tape:#跟踪tf.Variable类型数据的梯度变换
            #x:[b,28*28]
            #h1=x@w1+b1
            h1=x@w1+b1#[b,784]@[784,256]+[256]->[b,256]+[256]->[b,256]+[b,256]
            h1=tf.nn.relu(h1)#非线性转换
            h2=h1@w2+b2
            h2=tf.nn.relu(h2)
            out=h2@w3+b3#[b,10]

            #计算误差
            y_one_hot=tf.one_hot(y,depth=10)
            #均方差计算
            #mes=mean(sum(y-out)**2)
            loss=tf.square(y_one_hot-out)
            loss=tf.reduce_mean(loss)

        grads=tape.gradient(loss,[w1,b1,w2,b2,w3,b3])
        #w1=w1-lr*w1_grad
        '''
        w1=w1-lr*grads[0]#得到新的w1，不再是Variable,而是tensor
        b1 = b1 - lr * grads[1]
        w2 = w2 - lr * grads[2]
        b2 = b2 - lr * grads[3]
        w3 = w3 - lr * grads[4]
        b3 = b3 - lr * grads[5]'''
        #所以采用原地更新，保持数据类型不变
        w1.assign_sub(lr * grads[0])
        b1.assign_sub(lr * grads[1])
        w2.assign_sub(lr * grads[2])
        b2.assign_sub(lr * grads[3])
        w3.assign_sub(lr * grads[4])
        b3.assign_sub(lr * grads[5])

        if step%100==0:
            print(epoch,step,"loss",float(loss))
