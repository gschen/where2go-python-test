def abc(n,k):
    ls=list(range(1,n+1))
    if n==1:
        return
    else:
        index_=0
        for i in range(n-1):
            index_=(index_+(k-1))%len(ls)
            print(ls[index_])
            del ls[index_]
            if len(ls)==1:
                print(ls[0])
abc(10,3)