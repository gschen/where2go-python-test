a,b = map(int,input().split("/"))
if b!=0:
    if a>b:
        t=b
    else:
        t=a
    for i in range(1,t+1):
        if(a%i==0) and b%i==0:
            m = i
            a = a/m
            b = b/m
    print("%d/%d"%(a,b))