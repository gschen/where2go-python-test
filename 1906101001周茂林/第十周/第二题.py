'''
有n个人围成一圈，顺序排号。
从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
'''
def qq(n):
    l = list(range(1,n+1))
    while len(l) > 3:
        del l[2]
        a,b = l[0],l[1]
        l.remove(a)
        l.remove(b)
        l.extend([a,b])
    if 2 <= len(l) <= 3:
        print(l[1])
    if len(l) == 1:
        print(l[0])
qq(12)