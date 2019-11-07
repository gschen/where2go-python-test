def addpower(n):
    t=1
    sum=0
    while t<=n:
        sum+=t**2+1
        t+=1
    return sum
print(addpower(2))