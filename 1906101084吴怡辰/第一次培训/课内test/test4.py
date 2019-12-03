def xuanren(n):
    l = list(range(1,n + 1))#将给定的人创建一个list
    x = 0                 #添加一个统计变量，方便我们将需要剔除的人删掉
    while len(l)>1:
        l2=l[:]
        for i in range(0,len(l2)):
            x+=1
            if x%3==0:
                l.remove(l2[i])
    return l[0]