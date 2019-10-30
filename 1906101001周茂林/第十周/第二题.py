'''
有n个人围成一圈，顺序排号。
从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
'''
def qq(n):
    l = list(range(1,n+1))
    if n == 1:
        print(l[0])
    else:
        while len(l) != 1:
            aa = len(l) % 3
            for i in range(2-aa,n+1,3):
                del l[i]
        print(l[0])
qq(12)