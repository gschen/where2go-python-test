def raw(n):
    l=list(range(1,n+1))
    x=1
    if n%3==0:
        k=l[2::3]
        p=0
        while p==0:
            for i in l:
                for z in k:
                    if i==z:
                        x=0
                        break
                if x==1:
                    print(i)
    elif n%3==2:        
        k=l[2::3]
        p=0
        while p==0:
            if len(l)%3!=0:
                k=l[-2::3]
                for i in l:
                    for z in k:
                        if i==z:
                            x=0
                            break
                    if x==1:
                        print(i)
            else:
                k=l[2:3]
                for i in l:
                    for z in k:
                        if i==z:
                            x=0
                            break
                    if x==1:
                        print(i)

n=int(input("请输入人数n："))
raw(n)