#张量排序
import tensorflow as tf
'''
    Sort/argsort  完全排序/排序后的序号，原tensor不变
    Topk        前N个大的/小的
    Top-5 Acc
'''
a=tf.random.shuffle(tf.range(5))#得到一个一维数组并打乱
#假设a为[2,0,3,4,1]
tf.sort(a,direction='DESCENDING')#降序排列(不填默认升序),返回[4,3,2,1,0]
index=tf.argsort(a,direction='DESCENDING')
#返回[3,2,0,4,1],降序排列后的元素在原数组中的下标

#根据排序下标进行排序
tf.gather(a,index)#返回[4,3,2,1,0]

a=tf.random.uniform([3.3],maxval=10,dtype=tf.int32)
#生成3行3列的tensor，每个元素的范围为0-9的闭区间
tf.sort(a)#对每一行内的元素进行排序，不改变行的顺序,升序
idx=tf.argsort(a)#对每一行内的元素进行排序返回其在原数组中的下标，不改变行的顺序

'''
    假设a为 [[4,6,8],
             [9,4,7],
             [4,5,1]]
'''
res=tf.math.top_k(a,2)#默认降序，2表示取最大的前2位
res.indices
'''
    返回前两个大的在原数组中的下标
        [[2,1],
        [0,2]
        [1,0]]
'''
res.values
'''
    返回前两个大的的值
        [[8,6],
        [9,7]
        [5,4]]
'''
#top_k运用环境：假设同一样本预测多次，只要前k（k>1）次中有一次预测正确，就表明预测正确
#实战，课时43


