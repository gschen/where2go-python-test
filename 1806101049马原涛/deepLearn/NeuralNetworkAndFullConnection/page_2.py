import tensorflow as tf
#1.
x=tf.random.normal([4,784])
net=tf.keras.layers.Dense(512)
#实现wx+b的过程

out=net(x)#输出
out.shape#[4,512]

net.kernel.shape#[784,512],相当于w
net.bias.shape#[512],相当于b


#2.
net=tf.keras.layers.Dense(10)
net.build(input_shape=(None,4))
net.kernel.shape#[4,10]
net.bias.shape#[10]

net.build(input_shape=(None,20))
net.kernel.shape#[20,10]
net.bias.shape#[10]

net.build(input_shape=(2,4))
net.kernel.shape#[4,10]

#实现多个隐藏层的全连接
x=tf.random.normal([4,784])
#[784]->[512]->[256]->[128]->[10]
model=tf.keras.Sequential([
    tf.keras.layers.Dense(512,activation='relu'),
    tf.keras.layers.Dense(256,activation='relu'),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dense(10),
    ])
model.build(input_shape=[None,784])
model.summary()#类似与print

for p in model.trainable_variables:#这个会返回[w1,b1,w2,b2,w3,b3...]等可训练的参数
    print(p.name,p.shape)
    #打印每个variable的名字和shape

