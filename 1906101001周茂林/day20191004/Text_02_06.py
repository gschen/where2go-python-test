n = int(input())
a = 1
b = 1
c = 0
while a <= n:
    if a%2==0:
        c -= a/b
    else:
        c += a/b
    a += 1
    b += 2
print(round(c,3))