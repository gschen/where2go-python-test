#数学运算
'''
1. + - * /   可用于标量和向量或者矩阵
2. 平方:**，pow(x,多少次方),平方：square
3.开根：sqrt
4.整除：// ，求余：%
5.自然指数：exp ， 对数log
    tf.exp(),tf.math.log()
    这里的log只能以e为底,要想使用log2为底8为指，就用tf.math.log(8)/tf.math.log(2)
6.矩阵运算：@,matmul
7.linear layer
'''

'''
    
    [b,3,4]@[b,4,5]
    x=[b,3,4]
    y=[b,4,5]
    tf.matmul(x,y)
    表示有b个shape为[3,4],[4,5]的矩阵相乘
    如果matmul和@运算的矩阵shape相等，就表示为普通的矩阵乘法
    
    reduce_mean/max/min/sum
    表示求某个维度上的均值/最大值/最小值/和
    
    
'''