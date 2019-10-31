for i in range(101,201):
    a=2
    while i>a:
        if i%a==0:
            break
        else:
            a+=1
    if a==i:
        print(i)
#5