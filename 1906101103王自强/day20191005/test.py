x=int(input("请输入一个正整数："))
sum=0
i=1
n=1
while i<=x:
    s=(i/n)
    i=i+1
    n=n+2
    sum=sum+s*(-1)**i
print('sum=%.3f'%sum)