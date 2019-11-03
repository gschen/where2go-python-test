def dao(x):
    list1 = list(str(x))
    list1.reverse()
    return (int(list1[0]+list1[1]+list1[2]+list1[3]+list1[4]))



for n in range(10000,100000):
    for y in range(2,10):
        if n * y ==dao(n):
            print(n,y)