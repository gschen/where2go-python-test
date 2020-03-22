def lastRemaining(m,n):
    ls = [i for i in range(m)]
    x = n
    while m > 1:
        while m < n:
            n = n - (m % n)
        ls.pop(n-1)
        n = x+n-1
        m -= 1
    return ls[0]


print(lastRemaining(17,10))

