#输出方式
#部分激活函数的运用
import tensorflow as tf
'''
1.实数输出
2.概率输出（可能还会要求概率和为1）
3.。。。。

1.实数输出.简单
    linear reression
    naive classification with MSE
    other general prediction
    out=relu(x@w)+b
        logits

2.0<=yi<=1
    比如2分类中，概率大于0.5就判定为1，小于0.5就判断为0

    image generation
     将图片的[0-255]降至[0-1]

'''
#值压缩
'''
    2.0<=yi<=1
        out=relu(x@w+b)
        
        sigmoid  #一个y属于0到1的非线性函数
            所以可以把relu函数换为sigmoid函数，不仅可以做到非线性的转换，还可以将值压缩(投影)到0-1
            sigmoid的函数: y=1/(1+e**(-x)),直接用tf.sigmoid调用
'''

#运行如下代码查看效果
a=tf.linspace(-20,20,10)#生成-20到20的10个数
tf.sigmoid(a)


'''
    对于多分类问题sigmoid并不能很好的解决，比如10分类问题，数值范围是0-9
    此时就不仅要求单个值的概率是0-1，还要要求0-9中值的和为1
    那要如何解决这个问题
    softmax函数,内含归一化操作
    功能:非线性转换，值压缩0-1，概率和为1
    softmax 函数一般用在没用激活函数的最后一层，也就是输出层
'''



#补充
'''
    如果最后的值要求范围在-1到1
    可以用tanh函数
    tf.tanh
'''
