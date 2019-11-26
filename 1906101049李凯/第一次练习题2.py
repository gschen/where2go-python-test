def addpower():
    L=[]
    while n>1:
        for i in range(2,n+1):
            if n%i==0:
                n=int(n/i)
                L.append(i)
                break
return L