a=2
b=1
c=int(input("请输入项数："))
sum=0
for i in range(c):
    sum=a/b+sum
    a,b=(a+b),a
print(sum)