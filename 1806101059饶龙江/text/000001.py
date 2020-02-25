import numpy as np
n,m=input().split(' ')
if len(n) % 2 == 0:
    n_len = len(n) / 2
else:
    n_len = (len(n) // 2) + 1
n_len=int(n_len)
print(n_len)
lis1 = []
lis3 = []
for i in range(n_len):
    lis3.append('0')
for i in range(n_len):
    lis1.append('0')
for x in range(n_len):
    for y in range(1, 10):
        lis1[x] = str(y)
        lis3[x] = str(y - 1)
        a = ''.join(lis1)
        b = ''.join(lis3)
        if eval(a) ** 2 > eval(n) and eval(b) ** 2 <= eval(n):
            # lis3[x] = str(y-1)
            break
print(''.join(lis3))
