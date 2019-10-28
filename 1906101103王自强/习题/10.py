n = int(input('请输入你要求第几项和:'))
n2=1
m2=0
n1=1
m1=1
z2=0
for i in range(1,n+1):
    y=m2+m1
    x=n2+n1
    m2=m1
    n2=n1
    m1=y
    n1=x
    z1=x/y
    z3=z2+z1
    z2=z1
print('前{}项和为{}'.format(n,z3))
#10