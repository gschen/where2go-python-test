n=0
s=0
a=1
b=2
while n < 20:
    m=b/a
    c=a+b
    a=b
    b=c
    s=s+m
    n=n+1
print(s)