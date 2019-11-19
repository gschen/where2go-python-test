def raw(n):
    s=1
    for k in range(2,n-1):
        if n%k==0:
            s=0
    if s==1:
        print(n)
    return 
for n in range(2,101):
    raw(n)
            
                        