'''
将一个正整数分解质因数，例如输入90，打印90=2*3*3*5
'''
n=int(input())
while n>1:
    for i in range(2,n+1):
        if n%i==0:
            n=int(n/i)
            if n==1:
                print(i)
            else:
                print('{}'.format(i),end='*')
                break
