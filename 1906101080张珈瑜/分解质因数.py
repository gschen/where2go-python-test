def zys(n):
    l = list(range(1,n+1))
    l2 = []
    for i in l:
        for j in range(2,1):
            if i % j == 0:
                break
            else:
                l2.append(i)
        l2.insert(0,2)
        l3 = [n,'-']
        for i in l2:
            while n%i == 0:
                n = n/i
                l3.append(i)
                l3.append('*')
        l3.pop(-1)
        for j in l3:
            print(j,end='')
zys(90)