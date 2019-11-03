'''
2、	有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
'''
def er(n):
    l= list(range(1, n + 1))
    t=0
    while len(l)>1:
        l2=l[:]
        for i in range(0, len(l2)):
            t+=1
            if t%3==0:
                l.remove(l2[i])
    print("最后留下的为{}号".format(l[0]))
er(5)