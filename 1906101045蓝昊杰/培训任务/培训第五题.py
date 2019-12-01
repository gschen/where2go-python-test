for i in range(1,100000):
    m=str(i)
    n=len(m)
    if n==1:
        print(i)
    elif n==2:
        if m[0]==m[1]:
            print(i)
    elif n==3:
        if m[0]==m[2]:
            print(i)
    elif n==4:
        if m[0]==m[3] and m[1]==m[2]:
            print(i)
    else:
        if m[0]==m[4] and m[1]==m[3]:
            print(i)