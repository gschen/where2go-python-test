from functools import reduce
def raw(x,y):
    return x*10+y
s=[]
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                for e in range(1,10):
                    if int(reduce(raw,[a,b]))*int(reduce(raw,[c,d,e]))==int(reduce(raw,[a,d,b]))*int(reduce(raw,[c,e])) and a!=b and a!=c and a!=d and a!=e and b!=c and b!=d and b!=e and c!=d and c!=e and d!=e:
                        s.append(1)
print(len(s))


