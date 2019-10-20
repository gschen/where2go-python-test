#test
import tensorflow as tf
x=tf.random.normal([4,784])
model=tf.keras.Sequential([
    tf.keras.layers.Dense(512,activation='relu'),
    tf.keras.layers.Dense(256,activation='relu'),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dense(10),
    ])
model.build(input_shape=[None,784])#输入的shape
model.summary()#会打印出一些信息，具体是啥，自己打印
for p in model.trainable_variables:#这个会返回[w1,b1,w2,b2,w3,b3...]等可训练的参数
    print(p.name,p.shape)
    #打印每个variable的名字和shape