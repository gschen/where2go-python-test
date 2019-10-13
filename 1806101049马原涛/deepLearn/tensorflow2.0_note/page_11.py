#张量限辐:根据值裁剪/限制值的范围
import tensorflow as tf
'''
    clip_by_value
    relu
    clip_by_norm
    gradient clipping
'''

'''
    maximum(x,a)与minimum(x,a)
    1.maximum(x,a)
        a作为最大值，x比a小就返回a，x比a大就返回x本身
    2.minimum(x,a)
        a作为最小值,x比a大就返回a，x比a小就返回x本身
'''
x=tf.range(10)
tf.maximum(x,2)#返回[2,2,2,3,4,5,6,7,8,9]
tf.minimum(x,8)#返回[0,1,2,3,4,5,6,7,8,8]

#tf.clip_by_value(x,min,max)
#x属于min到max，返回x本身。x小于min返回min，大于max返回max
tf.clip_by_value(x,2,8)#将值限制在一个范围内
#返回[2,2,2,3,4,5,6,7,8,8]

#relu  小于0的都取0，大于0的取本身
b=x-5#[-5,-4,-3,-2,-1,0,1,2,3,4]
tf.nn.relu(b)#[0,0,0,0,0,0,1,2,3,4]
#等同于tf.maximun(b,0)

#clip_by_norm
'''
向量是有方向的，如果在对向量进行裁剪的时候，只缩放其中一个值
比如（x，y）只缩放x，可能会导致向量的方向变换，所以要做到等比例缩放
1.先求模长
2.用向量除模长，将其限制到0-1之间，再乘个数去达到我们要的范围
'''
a=tf.random.normal([2,2],mean=10)
tf.norm(a)#查看模长
aa=tf.clip_by_norm(a,15)#将模长限制在15，这样各个元素都会进行等比例缩放

#Gradient clipping

'''
    Gradient Exploding or vanishing
    梯度爆炸(梯度值过大)、梯度消失(梯度值过小)
    例：在做线性回归时，函数的整体方向由w1,w2,w3，b1,b2,b3共同决定
    所以做值限制就不能只限制其中一个
    new_grads,total_norm=tf.clip_by_global_norm([g_w1,g_w2,g_w3],25)
    25怎么得的，一般为w1、w2、w3的范数和
    将梯度值限制在合理范围内有利于函数稳定收敛
'''
