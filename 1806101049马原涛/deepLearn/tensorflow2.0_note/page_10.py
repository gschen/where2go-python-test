#填充与复制
import  tensorflow as tf
'''
    pad  填充
    tile  复制
    broadcast_to
'''
#pad
a=range(3)#[0,1,2]
b=tf.pad(a,[[1,2]])
#对于一维的,pad(a,[[l,r]]),l表示左边填充几个,r表示右边填充几个
#b=[0,0,1,2,0,0], 默认填充0

#对于二维的
a=tf.ones([2,2])
#tf.pad(a,[[y1,y2],[x1,x2]])
# y1表示矩阵上方加几行，y2表示矩阵下方加几行
#x1表示矩阵左边加几列，x2表示矩阵右边加几列
b=tf.pad(a,[[0,1],[1,1]])
'''
b=[ [0,1,1,0]
    [0,1,1,0]
    [0,0,0,0] ]
'''
#多维
a=tf.random.normal([4,28,28,3])
b=tf.pad(a,[[0,0],[2,2],[2,2],[0,0]])
b.shape#[4,32,32,3]


#tile 注意与broadcast_to区分
a=tf.range(3)#0,1,2
tf.tile(a,[1,2])#[0,1,2,0,1,2]
#tf.tile(a,[h,l])，h表示行扩充几倍，l表示列扩充几倍.先扩列后扩行
