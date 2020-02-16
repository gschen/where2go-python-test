def youxianji():
    n,m,t=map(int,input().split(' '))
    lis={}
    for i in range(m):
        a,b=map(int,input().split(' '))
        if a>=5:
            lis[b]=1
        else:
            lis[b] = 0
    number=0
    for i in lis:
        if lis[i]==1:
            number+=1
    return number