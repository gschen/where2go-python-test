#求奇数分之一序列前N项和
x = int(input('请输入一个数：'))
n = 1
S = 0
while n<=x:
    S = S+1/(2*n-1)
    n += 1
print('sum = %s'% '%.6f'% S)