aa = 'abcd'
for i in aa:
    for m in aa:
        for n in aa:
            if i != m and i != n and m != n:
                print(i,m,n)