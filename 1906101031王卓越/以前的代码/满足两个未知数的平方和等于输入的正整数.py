def raw(N):
    s = 0
    for X in range(0,N):
        for Y in range(0,X):
            if X**2+Y**2==N:
                print(X,Y)
                s += 1
    if s == 0:
        print('No Solution')
N=int(input("请输入一个正整数："))
raw(N)
