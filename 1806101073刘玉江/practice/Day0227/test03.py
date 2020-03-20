'''
给定一个正整数 N，找到并返回 N 的二进制表示中两个连续的 1 之间的最长距离。

如果没有两个连续的 1，返回 0 。
'''

N = 22
n = str(bin(N))[2:]
ls = []
a = 0
for i in n:
    if int(i) == 1:
        ls.append(a)
    a = a + 1
maxN = 0
for i in range(len(ls)):
    if i < len(ls)-1:
        if ls[i+1] - ls[i] > maxN:
            maxN = ls[i+1] - ls[i]
print(maxN)

