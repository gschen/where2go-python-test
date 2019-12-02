#分子
# def m(n):
    a,b=1,2
    while n>0
        a,b=b,a+b
        n=n-1
    return a
print('第20个分子是：'，m(20))
#分母
def k(n):
    a,b=1,1
    while n>0:
        a,b=b,a+b
        n=n-1
     return a
print('第20个分母是：'，k(20))
#各项和
def f(x):
    if x==1:
        return 2/1
    else:
        return(m(x)/k(x)+f(x-1))
    print(f(20))


