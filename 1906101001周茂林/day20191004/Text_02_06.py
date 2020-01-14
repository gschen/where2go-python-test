n = int(input())
a, b, c = 1, 1, 0
while a <= n:
    if a % 2 == 0:
        c -= a/b
    else:
        c += a/b
    a += 1
    b += 2
print(round(c, 3))
