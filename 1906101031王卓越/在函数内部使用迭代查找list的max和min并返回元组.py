def raw(n):
    k=max(n)
    l=min(n)
    for i in n:
        for x in n:
            if i==k and x==l:
                p=(i,l)
                print(p)
    return
n=list(input("输入一个列表值："))
raw(n)
#王卓越
        