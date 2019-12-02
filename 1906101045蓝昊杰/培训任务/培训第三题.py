a=2
b=1
s=n=0
while n<20:
    c=a+b
    s=s+a/b
    a,b=c,a
    n+=1
print(s)