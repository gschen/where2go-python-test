n = int(input('多少个开始球数的情况：'))
l = list(i for i in range(n))
for i in range(n):
    l[i] = int(input())

def qiuqiu(m):
    if m % 2 == 0: print(1)
    else: print(0)

for i in l:
    qiuqiu(i)


'''  1 3 7  输 0  赢 1
1   0
2   1
3   0
4   1
5   0
6   1
7   0
8   1
9   0
'''