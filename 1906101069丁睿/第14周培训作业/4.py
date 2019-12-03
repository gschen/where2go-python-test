N = int(input())
n = N
l = [11,5,2,1]
T = []
for i in l:
    while N >= i:
        N -= i
        T.append(i)
        T.append('+')
T.pop(-1)
print(n,'=',end='')
for k in T:
    print(k,end='')