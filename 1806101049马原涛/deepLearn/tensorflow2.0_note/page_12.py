import tensorflow as tf
#高阶op
'''
    where   #根据坐标选择
    scatter_nd  #根据坐标更新
    meshgrid    #生成坐标系
'''
#1.where只接受一个参数
'''
    where   只接受一个tensor，就是bool矩阵
    a [[true ,false,false]
       [false,true ,false]
       [false,false,true ]]
    a.shape->[3,3]
    where(a),会返回true的坐标
    以左上角第一个元素作为坐标原点
    所以第一个true的坐标为(0,0),第二个(1,1)，第3个(2,2)
    
'''
a=tf.random.normal([3,3])
mask=a>0#大于0的值变为true,小于0的变为false。mask与a的shape相同
tf.boolean_mask(a,mask)#取出a的值，该值在mask中的对应位置为true

indices=tf.where(mask)#取出mask中为true的位置的坐标
tf.gather_nd(a,indices)#取出对应坐标的值

#2.where接受3个参数
#where(cond,a,b)
'''
    根据cond矩阵中的True来选择对应位置的A矩阵中的元素，
    False来选择对应位置的B矩阵中的元素，组建一个新的矩阵
    作用：有目的性的对a、b矩阵的值进行筛选
'''
#例
a=tf.ones([3,3])
b=tf.zeros([3,3])
c=tf.constant([True,True,False],[True,False,False],[False,True,False])
tf.where(c,a,b)
'''
返回 [[1,1,0]
      [1,0,0]
      [0,1,0]]
'''


#scatter 有目的性的根据坐标对值进行更新
'''
    tf.scatter_nd(
    indices,      根据坐标改变对应底板上的值
    updates,
    shape         shape给定底板，一维二维多维，所有值默认为0
    
'''
indices=tf.constant([[4],[3],[1],[7]])
updates=tf.constant([9,10,11,12])
#底板上下标4的位置更新为9，下标3的位置更新为10，下标1的位置更新为11，下标7的位置更新为12
shape=tf.contant([8])#底板是一维，值全为0、长度为8的tensor
tf.scatter_nd(indices,updates,shape)
#返回[0,11,0,10,9,0,0,12]
#tf.scatter_nd只能更新底板为0的值
#scatter使用复杂，详情看课时47、48

#meshgrid  应用在48课时，不好笔述，记得复习
'''
给定x和y的范围，生成[x1,y1],[x2,y2],[x3,y3]...等范围内的坐标
'''
y=tf.linspace(-2.,2.,5)#生成-2.到2.的五个值,均匀分布
x=tf.linspace(-2.,2.,5)
point_x,point_y=tf.meshgrid(x,y)
point_x.shape#[5,5],共25个值，每一列上的值都相等
point_y.shape#[5,5],共25个值，每一行上的值都相等

points=tf.stack([point_x,point_y],axis=2)
#合并point_x和point_y，组成坐标轴，增加一个维度
points.shape#[5,5,2]5行5列，2个通道，也就是x、y组合成一个坐标点

