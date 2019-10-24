n = 0
while True:
    a = (n+100)**(1/2)
    c = round(a)
    b = (n+100+168)**(1/2)
    d = round(b)
    if a==c and b==d:
        print(n)
    n += 1