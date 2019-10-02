def pai(n):
    if n == 0 or n == 1:
        return 1
    if n > 1:
        return n * pai(n - 1)


def kk(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    if n > 1:
        k = 2 * n + 1
        return k * kk(n - 1)


aa = eval(input())
sss = 0
a = 0
dan = 1
while dan > aa:
    dan = pai(a) / kk(a)
    a += 1
    sss = sss + dan

print("{:.6f}".format(sss * 2))



