def raw(*n):
    l=list(n)
    x=int(input("请给定一个值:"))
    for a in l:
        for b in l:
            if a+b==x:
                p=[]
                for k in range(0,9):
                    for q in range(0,k):
                        if l[k]==a and l[q]==b:
                            s=[k,q]
                            print(s)  
    return
raw(1,2,3,4,5,6,7,8,9)