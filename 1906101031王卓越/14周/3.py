def raw(a,b,n,k):
    if n<19:
        k=k+(a+b)/a
        return raw(a+b,a,n+1,k)
    if n==19:
        return k
print(raw(2,1,0,2))
 
    