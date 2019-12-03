"""现知道有些数为回文数，例如121，242，12321。我们就称这种数字为回文数，像10，14，467就不为回文数。先要求你用程序将区间[1，100000]内所有的回文数输出。"""
# i=int(input("num"))#
l=[]
a=[]
c=[]
d=[]
f=[]
for s in range(1,10):
    t=str(s)
    if len(t)== 1 :
        f.append(t)
        print(t)
for g in range(1,100):
    m=str(g)
    if len (m) == 2 and  m[0]==m[1] :
        d.append(m)
        print(m)
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
print("sum=",len(a)+len(l)+len(c)+len(m)+len(f))


