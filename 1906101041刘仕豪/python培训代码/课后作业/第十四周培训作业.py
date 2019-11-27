'''
给定一个一维数组，你需要删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度和新的数组。
'''
#1
def delsame(l):
    l2 = []
    for i in l:
        if i not in l2:
            l2.append(i)
    return len(l2),l2
#2
t = 0
for a in range(1,10):
    for b in range(1,10):
        for c in range(1, 10):
            for d in range(1, 10):
                for e in range(1, 10):
                    if (a*10+b)*(c*100+d*10+e) == (a*100+d*10+b)*(c*10+e) and a!=b and a!=c and a!=d and a!=e and b!=c and b!=d and b!=e and c!=d and c!=e and d!=e:
                        t+=1
print(t)
#3
def fibsum(n):
    a = 2
    b = 1
    c = a / b
    for i in range(0, n-1):
        a, b = a + b, a
        c += a / b
    return c
#4
N = int(input())
n = N
l = [11,5,2,1]
l2 = []
for i in l:
    while N >= i:
        N -= i
        l2.append(i)
        l2.append('+')
l2.pop(-1)
print(n,'=',end='')
for k in l2:
    print(k,end='')

#5
