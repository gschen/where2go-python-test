n = 0
while True:
    A = (n+100)**(1/2)
    a = round(A)
    if a == A:
        B = (n+100+168)**(1/2)
        b = round(B)
        if b == B:
            print(n)
    n += 1