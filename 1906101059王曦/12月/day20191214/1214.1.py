n = int(input())
if n > 0 and n < 6:
    L =[]
    a = n+1
    b = n+2
    c = n+3
    L.append(n)
    L.append(a)
    L.append(b)
    L.append(c)
    for i in L:
        for j in L:
            for k in L:
                if i!= j and i !=k and j != k:
                    m= i*100+j*10+k
                    print(m)