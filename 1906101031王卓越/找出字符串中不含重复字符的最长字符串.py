def raw(n):
    k=[]
    for b in range(len(n)+1):
        for a in range(1,b):
            if len(n[a:b])==len(set(n[a:b])):
                l=n[a:b]
                k.append(len(l))         
    return max(k)
print(raw('abcabc'))
