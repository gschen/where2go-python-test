#用迭代的方法找出输入数组的最大最小值
def jiang2(l):
    import random
    n = random.choice(l)
    m = 0
    for i in l:
        if i > m:
            m = i
        elif i < n:
            n = i
    return m,n
l = list(map(int,input('请输入一个数组：').split()))
print(jiang2(l))
