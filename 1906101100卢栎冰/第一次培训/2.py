L=[]
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                for e in range(1,10):
                    if a!=b and a!=c and a!=d and a!=e and b!=c and b!=d and b!=e and c!=d and c!=e and d!=e:
                        if(a*10+b)*(c*100+d*10+e)==(a*100+d*10+b)*(c*10+e):
                            l=[a*10+b,c*100+d*10+e,a*100+d*10+b,c*10+e]
                            for i in l:
                                l.append(i)

m=len(l)/4
print('如此计算能有的种类数：%0.f' %m)
