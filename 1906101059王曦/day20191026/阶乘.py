def jie(x):
    a = 1
    while x > 0:
        a = a*x
        x -= 1
    return a


n = 20
c = 0
while n > 0:
    s = jie(n)+c
    n -= 1
    print(s)
    break
