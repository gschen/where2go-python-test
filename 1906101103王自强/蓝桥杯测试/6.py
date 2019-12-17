'''标题：打印大X

如下的程序目的是在控制台打印输出大X。
可以控制两个参数：图形的高度，以及笔宽。'''
h,x=map(int,input().split(' '))
m=h-x-1
i=0
while m>0:
     print('.' * i + '*'*x + "." * (m) + '*'*x + '.' * i)
     m-=2
     i+=1
s=q=h+x-1-2*(i)
while q>=x:
     print('.'*i+'*'*q+'.'*i)
     q-=2
     i+=1
q=q+4
i=i-1
while q<=s:
     i=i-1
     print('.' * i + '*' * q + '.' * i)
     q+=2
m=m+2
i-=1
while m<=h-x-1:
     print('.' * i + '*' * x + "." * (m) + '*' * x + '.' * i)
     m+=2
     i-=1

