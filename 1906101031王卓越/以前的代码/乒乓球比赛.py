l=('a','b','c')
k=('x','y','z')
for i in l:
    for o in k:
        j=(i,o)
        h=(l[0],k[0])
        p=(l[2],k[0])
        q=(l[2],k[2])
        if j!=h and j!=p and j!=q:
            print(j)