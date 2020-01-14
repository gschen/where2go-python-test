# 求整数段和
A,B = map(int,input('请输入两个数：').split())
i = 0
S = 0
while A<=B:
    S = S + A
    print('{:>5}'.format(A),end='')
    A += 1
    i += 1
    if i == 5:
        print('\n',end='')
        i = 0
print('\n',end='')
print('sum = %d'% S)
