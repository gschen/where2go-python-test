for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            if c+b*10+a*100==a**3+b**3+c**3:
                print(c+b*10+a*100)