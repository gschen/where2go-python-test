#找出所有(a*10+b)*(c*100+d*10+e) == (a*100+d*10+b)*(c*10+e)的情况
s = 0
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                for e in range(1,10):
                    if a!=b and a!=c and a!=d and a!=e and b!=c and b!=d and b!=e and c!=d and c!=e and d!=e:
                        if (a*10+b)*(c*100+d*10+e) == (a*100+d*10+b)*(c*10+e) and (a*10+b)!=(c*10+e):
                            s+=1
print(s)