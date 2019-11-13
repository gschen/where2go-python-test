def tnangles(x):
    l_1=[1]
    l_2=[1,1]
    if x==1:
        print(l_1)
    elif x==2:
        print(l_1)
        print(l_2)
    else:
        print(l_1)
        print(l_2)
        for i in range(1,x):
            l_1=l_2[:]
            l_2[2:]=l_2[1:]
            for j in range(i):
                l_2[j+1]=l_1[j]+l_1[j+1]
            print(l_2)
tnangles(9)