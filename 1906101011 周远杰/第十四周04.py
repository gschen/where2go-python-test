def zhou(x):
    if x>=11:
        print(11)
        return zhou(x-11)
    elif 5<=x<11:
         print(5)
         return zhou(x-5)
    elif 2<=x<5:
         print(2)
         return zhou(x-2)
    elif x==1:
        print(1)
        return zhou(x-1)
N=int(input())
zhou(N)