a,b=map(int,input().split())
a='%04d' % a
b='%04d' % a
c=a[0:2]
d=a[2:4]
e=b[0:2]
f=b[2:4]
a=int(a)+int(e)
b=int(d)+int(f)
if b>=60:
    a=a+1
    b=b-60
if b<0:
    a=a-1
    b=b+60
print(a,b,sep='')