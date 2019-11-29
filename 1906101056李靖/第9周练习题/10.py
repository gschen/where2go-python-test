n = 20
a=2
b=1
c=a/b
for i in range(n-1):
    a,b=a+b,a
    c+=a/b
print(c)