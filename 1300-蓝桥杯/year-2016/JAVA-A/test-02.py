for i in range(1,237):
    n = 0
    for s in range(i,327):
        n = n+s
        if n >= 236:
            break
    if n == 236:
        print(i)
        break
