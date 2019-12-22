a,b=map(int,input().split(' '))
a=str(a)
n=len(a)-1
sum=0
for i in a:
    sum+=int(i)*b**n
    n-=1
print(sum)