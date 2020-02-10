list1 = range(1,21)
for a in list1:
    for b in list1:
        for c in list1:
            for d in list1:
                e = 0
                if a>b>c>d and 1/a+1/b+1/c+1/d==1:
                    print(a,b,c,d)
