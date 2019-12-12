def raw(num):
    for a in num:
        for b in num:
            for c in num:
                if a+b+c==0 and a!=b!=c:
                    k=[a,b,c]
    return k
print(raw([ -1,0,1,2,-1,-4]))
