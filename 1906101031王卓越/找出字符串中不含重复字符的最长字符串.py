def raw(n):
    a=0
    k=[]
    for b in range(a+1,len(n)):
        for s in range(1,b):
            if n[a]==n[b]:
                l=n[a:b]
                a=a+1 
                print(l)
                k.append(len(l))
        #elif n[b]==n[-1] and n[a]!=n[b]:
         #   l=n[a:b]
         #   a=a+1 
         #   k.append(len(l))           
    return max(k)
print(raw('ssdajdadjsajuurs'))
