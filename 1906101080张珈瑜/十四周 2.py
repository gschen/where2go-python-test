M=0
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                for d in range(1,10):
                    for e in range(1,10):
                        if a!=b and a!=c and a!=d and a!=e and b!=c and b!=d and b!=e and c!=d and c!=e and d!=e and e!=a:
                            n=(a*10+b)*(c*100+d*10+e)
                            m=(c*10+e)*(a*100+d*10+b)
                            if n/m==1:
                                M+=1
print(M)