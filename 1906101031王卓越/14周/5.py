for a in range(1,100001):
    k=list(str(a))
    k.reverse()
    l=(''.join(k))
    if a==int(l):
        print(a)