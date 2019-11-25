def xuanren(n):
    l= list(range(1, n + 1))#先将给定的人创建成一个list
    t=0                     #添加一个统计变量，方便我们将需要剔除地人删掉
    while len(l)>1:         #
        l2=l[:]             #拷贝一个list，接下来可以通过条件移除之前list里面的元素
        for i in range(0, len(l2)):
            t+=1
            if t%3==0:          #计数器t没加三次就移除一个人
                l.remove(l2[i])
    return l[0]   #当只剩下最后一个人的时候返回序号



