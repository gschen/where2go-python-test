n=int(input('请输入你要求的项数:'))
n_2=0
n_1=1
x=1
for i in range(2,n+1):
    x=n_2+n_1
    n_2=n_1
    n_1=x
print('第{}项数是{}'.format(n,x))