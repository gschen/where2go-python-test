'''5.九数组分数
1,2,3...9 这九个数字组成一个分数，其值恰好为1/3，如何组法'''
box=['1','2' ,'3','4','5','6','7','8','9']
for a in box:
    for b in box:
        for c in box:
            for d in box:
                for e in box:
                    for f in box:
                        for g in box:
                            for h in box:
                                for i in box:
                                    if a!=b and a!=c and a!=d and a!=e and a!=f and a!=g and a!=h and a!=i:
                                        if b!=c and b!=d and b!=e and b!=f and b!=g and b!=h and b!=i:
                                            if c!=d and c!=e and c!=f and c!=g and c!=h and c!=i:
                                                if d!=e and d!=f and d!=g and d!=h and d!=i:
                                                    if e!=f and e!=g and e!=h and e!=i:
                                                        if f!=g and f!=h and f!=i:
                                                            if g!=h and g!=i:
                                                                if h!=i:
                                                                    if int(a+b+c+d)*3==int(e+f+g+h+i):
                                                                        print(a+b+c+d,e+f+g+h+i)