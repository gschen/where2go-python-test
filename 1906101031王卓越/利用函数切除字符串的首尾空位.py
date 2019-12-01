def raw(n):
    for i in range(0,len(n)):
        while n[i]==" ":
            n=n[i+1:]
            if n[-i]==" ":
                n=n[:-i-1]
        return n
print(raw('   dadasdssadsa  '))
        
