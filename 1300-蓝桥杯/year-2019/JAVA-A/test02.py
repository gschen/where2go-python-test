a=1
b=1
c=1
i=3
result=20190324
while i<20190324:
    i+=1
    d=a%10000+b%10000+c%10000
    a=b%10000
    b=c%10000
    c=d
print(str(c)[-4:])