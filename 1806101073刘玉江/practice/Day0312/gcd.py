def gcd(x,y):
    while y != 0:
        x,y = y,x%y
    return x


print(gcd(1200,600))