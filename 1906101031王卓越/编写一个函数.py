def raw(n):
    if n%2==0:
        k=2
        s=0
        for i in range(0,n//2):
            x=1/k
            k=k+2
            s=s+x
        print(s)    
    elif n%2==1:
        p=1
        q=0
        for i in range(0,n//2):
            y=1/p
            p=p+2
            q=q+y
        print(q)
    return
n=int(input("请输入n:"))
raw(n)