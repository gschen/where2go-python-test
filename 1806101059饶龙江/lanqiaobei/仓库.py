n=eval(input())
m=eval(input())
a=0
b=0
c=m
for i in range(1,n+1,3):
    if i<n:
        a+=1
for j in range(3,n+1,3):
    if i <=n:
        b+=1
for y in range(1,m+1):
    if y%6==0:
        c-=1
x=(a+b)*c

print(x)





