for i in range(1,100000):
    if i in range(1,10):
        print(i)
for i in range(10,100):
    a=str(i)
    if a[0]==a[1]:
        print(a)
for i in range(100,1000):
    b=str(i)
    if b[0]==b[-1]:
        print(b)
for i in range(1000, 10000):
    c = str(i)
    if c[0] == c[-1] and c[1]==c[-2]:
        print(c)
for i in range(10000, 100000):
    d = str(i)
    if d[0] == d[-1] and d[1]==d[-2] and d[2]==d[-3]:
        print(d)
#way2
for i in range(1,100000):
    if i==int(str(i)[::-1]):
        print(i)
