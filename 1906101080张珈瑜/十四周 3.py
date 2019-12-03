n=int(input())
a=2
b=1

sum=0
for i in range(n):
    c=a/b
    sum=sum+c
    a,b=a+b,a
print(sum)
