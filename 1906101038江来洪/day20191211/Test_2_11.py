#求平方与倒数序列的部分和
m,n = map(int,input('请输入两个数：').split())
S = 0
while m<=n:
    S = S+m**2+1/m
    m += 1
print('sum = %s'% '%.6f'% S)