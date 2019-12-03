a=2
b=1
s = 0
for i in range(20):
    s=s+a/b
    a,b=a+b,a
print(s)