for a in range(-100,99999):
    b=int((a+100)**0.5)
    c=int((a+268)**0.5)
    if b**2-100==a and c**2-268==a:
        print(a)