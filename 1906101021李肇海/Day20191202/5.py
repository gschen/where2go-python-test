for i in range(1,1000):
    x=str(i)
    if len(x)==3 and x[0]==x[2]:
        l.append(x)
        print(x)
for s in range(1000,10000):
    y=str(s)
    if len(y)==4 and y[0] == y[3] and y[1] == y[2]:
        print(y)
        a.append(y)
for b in range (10000,100000):
    z=str(b)
    if len(z)==5 and z[0] == z[4] and z[1] == z[3]:
        print(z)
        c.append(z)
print("sum=",len(a)+len(l)+len(c))