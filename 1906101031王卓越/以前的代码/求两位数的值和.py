def raw(n):
    if 10<=n and 10<=100:
        if 1000<=n*809 and n*809<10000:
            if 10<=8*n and 8*n<=100:
                print("??的值为：",n)
                print("809*??的值为：",809*n)
    return
for n in range(10,100):
    raw(n)
