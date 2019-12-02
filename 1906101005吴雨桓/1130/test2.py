#循环遍历 abcde互不相等 ab*cde=adb*ce
#计算个数


l=[]
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                for e in range(1,10):
                    if a!=b and a!=c and a!=d and a!=e and b!=c and b!=d and b!=e and c!=d and c!=e and d!=e:
                        if (a*10+b)*(c*100+d*10+e) == (a*100+d*10+b)*(c*10+e):
                            l.append((a*10+b)*(c*100+d*10+e) == (a*100+d*10+b)*(c*10+e))
print(len(l))
