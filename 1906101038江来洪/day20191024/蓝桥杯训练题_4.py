#斐波那契数列
def peibo(x):
    a = -1
    b = 1
    n = 0
    while n<x:
        s = a+b
        a = b
        b = s
        n += 1
    return s
x = int(input('你要求第几项：'))
print(peibo(x))
