from random import*
l=list(range(0,1000))
k=sample(l,10)
#sample意思表示从l列表中选取10个数
z=sorted(k)
#sorted将代码从大到小的顺序依次排列
z.reverse()
#reverse将已经知道的代码反过来排序
print(z)