#2有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
n=int(input('请输入围圈人数：'))
l_1=list(range(1,n+1))
i=0
while len(l_1)>1:
    l_2=l_1[:]
    for o in range(len(l_2)):
        i+=1
        if i%3==0:
            l_1.remove(l_2[o])
print('最后留下来的是原来的第{}号'.format(l_2[0]))