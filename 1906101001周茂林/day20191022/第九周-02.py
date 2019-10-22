for x in range(-100,99999):
    a = int((x + 100)**0.5)
    b = int((x + 268)**0.5)
    if a**2-100==x and b**2-268==x :
        print(x)