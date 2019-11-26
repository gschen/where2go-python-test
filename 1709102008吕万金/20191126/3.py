# print([x for x in range(1,101)])
# print([x for x in range(1,101) if x !=3 and x!=75])
for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                for e in range(0,10):
                    for k in range(0,10):
                        if (a*10000 +b*1000+c*100+d*10+e)*k==e*10000+d*1000+c*100+b*10+a and a!=b and a!=c and a!=d and a!=e and a!=k and b!=c and b!=d and b!=e and b!=k and c!=d and c!=e and c!=k and d!=e and d!=k and e!=k:
                            print(a,b,c,d,e)

