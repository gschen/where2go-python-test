def raw(n):
    for a in range(4,n):
        for b in range(1,a):
            for c in range(1,b):
                z=c-c
                if (1/n)+(1/a)+(1/b)+(1/c)==1:
                    print(n,a,b,c,z)
    return n,a,b,c,z
for n in range(5,21):
    raw(n)