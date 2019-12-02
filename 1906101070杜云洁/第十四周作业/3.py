a=1
b=2
sum=0
for i in range(20):
    sum=a/b+sum
    a,b=(a+b),a
print(sum)