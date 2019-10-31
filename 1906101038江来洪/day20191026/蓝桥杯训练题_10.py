#2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前x项之和
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
y = 0
for i in range(1,x+1):
    c = peibo(i+3)
    d = peibo(i+2)
    y = y+(c/d)
print('该数列的前%d项之和为%f' % (x,y))