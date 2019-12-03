def Ta(x):
    if x>=11:
        print(11)
        return Ta(x-11)
    elif 5<=x<11:
        print(5)
        return Ta(x-5)
    elif 2<=x<5:
        print(2)
        return Ta(x-2)
    elif x == 1:
        print(1)
        return Ta(x-1)


x=int(input())
Ta(x)
