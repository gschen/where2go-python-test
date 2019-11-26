'''
有n个人围成一圈，顺序排号。
从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
'''


def qqmm(n):
    li = list(range(1, n+1))
    while len(li) > 3:
        del li[2]
        a, b = li[0], li[1]
        li.remove(a)
        li.remove(b)
        li.extend([a, b])
    if 2 <= len(li) <= 3:
        print(li[1])
    if len(li) == 1:
        print(li[0])


n = 12
qqmm(n)
