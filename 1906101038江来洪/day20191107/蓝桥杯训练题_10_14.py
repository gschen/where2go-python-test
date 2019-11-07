#计算出选手刚好获100分的所有可能
def erjin(x):
    list = []
    while x >= 1:
        y = x%2
        x = x//2
        list.insert(0,str(y))
    return (''.join(list))
for x in range(1024):
    list1 = list(erjin(x))
    while len(list1) < 10:
        list1.insert(0,str(0))
    n = 1
    a = 10
    for i in list1:
        if int(i) == 0:
            a -= n
        else:
            a *= 2
        n += 1
    if a == 100:
        print(''.join(list1))