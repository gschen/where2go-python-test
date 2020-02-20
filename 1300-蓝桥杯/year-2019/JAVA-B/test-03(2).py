# a=1
# b=1
# c=1
# x=0
# while x<20190324:
#     print(a)
#     print(b)
#     print(c)
#     a=a+b+c
#     b=b+c+a
#     c=c+a+b
#     x+=1
a=1
b=1
c=1
for i in range(3,20190324):
    sums=(a+b+c)%10000
    a=b
    b=c
    c=sums
print(c)



