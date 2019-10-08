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

#clip_by_norm 课时45，6分左右