#数据统计
import tensorflow as tf
'''
    tf.norm     范数 
    tf.reduce_min/max
    tf.argmax/argmin    最大最小值位置
    tf.equal            张量笔记
    tf.unique
'''
#向量的2范数
a=tf.ones([2,2])
tf.norm(a)#（1^2+1^2+1^2+1^2）^0.5
#返回2,等同于下行
tf.sqrt(tf.reduce_sum(tf.square(a)))

#1范数
tf.norm(a,ord=1)

tf.norm(a,ord=1,axis=0)#求每列的1范数
tf.norm(a,ord=1,axis=1)#求每行的1范数

#reduce_min/max/mean
a=tf.random.normal([4,10])
tf.reduce_min(a)#求整个a中的最小值

tf.reduce_min(a,axis=1)
#求a中第二个维度的最小值，有4个,因为有4个10

#argmax/argmin
a=tf.random.normal([4,10])
tf.argmax(a)#不写axis默认为0，所以会返回10个最大值的下标

#equal
a=tf.constant([1,2,3,2,5])
b=tf.range([5])
tf.equal(a,b)#b和a的对应位做比较，相同返回true，不同返回false
#可以通过查看true和false的个数来判断有多少相等和不等

#去除重复元素 unique
a=tf.range(5)
tf.unique(a)#返回[0,1,2,3,4]和[0,1,2,3,4]
b=tf.constant([4,2,6,4,8,2])
tf.unique(b)
#返回两部分[4,2,6,8]和[0,1,2,0,4,1]
#后面那个表示各个元素的下标，重复元素的下标改为改元素第一次出现的下标



