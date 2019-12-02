def wu(x):
    if x>=11:
        print(11)
        return wu(x-11)
    elif 5<=x<11:
        print(5)
        return wu(x-5)
    elif 2<=x<5:
        print(2)
        return wu(x-2)
    elif x == 1:
        print(1)
        return wu(x-1)


x=int(input())
wu(x)


