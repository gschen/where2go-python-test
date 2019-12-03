def sums(n,a,b,sum):
    sum = sum+(a+b)/a
    if n<19:
        return sums(n+1,a+b,a,sum)
    if n==19:
        return sum
print(sums(1,2,1,2))
