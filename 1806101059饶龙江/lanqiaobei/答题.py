for i in range(0,1024):
    b=10
    x='{:0>10}'.format(bin(i)[2:])
    for j in range(len(x)):
        if x[j] =='1':
            b=b*2
        else:
            b = b-(j+1)
    if b==100:
        print(str(x))
