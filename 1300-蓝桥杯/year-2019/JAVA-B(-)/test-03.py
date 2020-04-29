a = 1
b = 1
c = 1
d = 0
for i in range(20190321):
    d = (a+b+c) % 10000
    a = b % 10000
    b = c % 10000
    c = d % 10000
    print(d)
print(d)