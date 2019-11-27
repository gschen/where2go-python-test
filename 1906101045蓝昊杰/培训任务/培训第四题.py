n=int(input())
a=b=c=d=0
while n>=11:
    n-=11
    a+=1
    print(11)
while n<11 and n>=5:
    n-=5
    b+=1
    print(5)
while n<5 and n>=2:
    n-=2
    c+=1
    print(2)
if  n==1:
    d+=1
    print(1)
