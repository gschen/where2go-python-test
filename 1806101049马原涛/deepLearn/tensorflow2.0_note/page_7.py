import tensorflow as tf
#张量的合并与分割
'''
    tf.concat  拼接
    tf.split    拆分
    tf.stack    堆叠
    tf.unstack

'''

#concat
'''
    [class1-4,students,scores]->[4,35,8]
    [class5-6,students,scores]->[2,35,8]
    一份1-4班的成绩资料，一份5-6班的成绩资料
    合并后的shape就是[6,35,8]
'''
a=tf.ones([4,35,8])
b=tf.ones([2,35,8])
#合并
c=tf.concat([a,b],axis=0)
#axis表示在哪一个维度上进行合并
c.shape()#返回[6,35,8]
a=tf.ones([4,32,8])
b=tf.ones([4,3,8])
c=tf.concat([a,b],axis=1)
c.shape()#返回[4,35,8]
#需要拼接的维度axis可以不等，其他要相等

#stack
'''
    将两个学校的数据进行拼接,拼接后仍然要对2学校进行区分
    school1[classes,students,scores]
    school2[classes,students,scores]
    拼接后的shape：[schools,classes,students,scores]
'''
a=tf.ones([4,35,8])
b=tf.zeros([4,35,8])
c=tf.stack([a,b],axis=0)#在0之前创作一个新的维度
c.shape()#返回[2,4,35,8]
#所有维度都必须相等

#unstack，按维度数拆分
a=tf.ones([2,4,35,8])
aa,bb=tf.unstack(a,axis=0)#a[0].shape=2,就拆为2个，所以需要2个tensor来保存
aa.shape()#[4,35,8]
bb.shape()#[4,35,8]
cc=tf.unstack(a,axis=1)#拆为4个,保存在cc这个tensor中
#读取第一个就是cc[0],cc[0].shape->[2,35,8].第二个就是cc[1]...

#split 可以指定打散的数量和比例
a=tf.ones([2,4,35,8])
b=tf.split(a,axis=3,num_or_size_splits=2)
#拆分为两个，8/2=4，8拆分为2个4

c=tf.split(a,axis=3,num_or_size_splits=[2,2,4])
#拆分为3个tensor，c[0],c[1],c[2]
#8拆分为2、2、4

