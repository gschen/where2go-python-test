
def sumZero(n):
    if n == 1:
        return 0
    if n>=0:
        l = list(range(1,n))
        a = -sum(l)
        l.append(a)
        return l