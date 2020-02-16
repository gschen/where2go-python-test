def zhexian(x,y):
    n=max(abs(x),abs(y))
    sn=4*(n-1)*n
    sum=0
    px=-n
    py=-n
    d1=x-px
    d2=y-py
    if y>x:
        sum+=(d1+d2)
    else:
        sum+=(8*n-d1-d2)
    return sum+sn
print(zhexian(0,1))