def f1(x):
    if x>=11:
        print(11)
        return f1(x-11)
    elif 5<=x<11:
        print(5)
        return f1(x-5)
    elif 2<=x<5:
        print(2)
        return f1(x-2)
    elif x==1:
        print(1)
        return f1(x-1)
N = int(input())
f1(N)