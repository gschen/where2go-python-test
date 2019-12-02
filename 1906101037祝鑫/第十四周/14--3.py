a = 2
b = 1
c = a/b
for i in range(0,19):
    a,b = a+b,a
    c += a/b
print(c)