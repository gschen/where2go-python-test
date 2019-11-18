N = int(input())
n = N
lis = [11,5,2,1]
lis2 = []
for i in lis:
    while N >= i:
        N -= i
        lis2.append(i)
        lis2.append('+')
lis2.pop(-1)
print(n,'=',end='')
for k in lis2:
    print(k,end='')