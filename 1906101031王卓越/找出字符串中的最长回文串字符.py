def raw(n):
    s=[]
    for a in range(0,len(n)):
        for b in range(a+1,len(n)):
            if n[a]==n[b]:               
                l=n[a:b+1]
                print(l)
                break
                s.append(len(l))
            #for k in range(0,len(n)):
    return s
print(raw("babadwdadaafdf"))