#找出输入范围内数字的各位数字的平方和大于原数字的数字
N,M = map(int,input().split())
for i in range(N,M+1):
    s = 0
    for n in str(i):
        s = s+int(n)**2
    if s>i:
        print(i)
