for m in range(10000,100000):
    p=int(str(m)[::-1])
    for k in range(1,10):
        if m*k==p and str(m)[0]!=str(m)[1] and str(m)[2]!=str(m)[3] and str(m)[4]!=str(m)[0] and str(m)[2]!=str(m)[4]:
            print(m)