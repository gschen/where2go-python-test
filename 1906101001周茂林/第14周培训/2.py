'''
正整数分解
'''
N = int(input())
n = N
lis = []
for i in range(2, N+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        lis.append(i)
lis2 = []
while N != 1:
    for p in lis:
        lis2.append(p)
        N /= p
        break
print(lis2)
