'''
RSA解密
'''
n = 55
d = 3
C = 19
lis1 = list(x for x in range(2, n))
for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            lis1.remove(i)
            break
for i in lis1:
    for j in lis1:
        if j * i == n:
            p, q = i, j
            break
for e in range(1, n):
    if (d * e) % ((p - 1) * (q - 1)) == 1:
        break
X = C**e % n
print(X)