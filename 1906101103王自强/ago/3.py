a,b=eval(input('输入两个整数，并用逗号隔开：'))
c=d=0
if a>b:
    a,b=b,a
while a%b!=0:
    c=a%b
    a=b
    b=c
d=int(a*b/c)
print('最小公约数是{}\n最大公倍数是{}'.format(c,d))