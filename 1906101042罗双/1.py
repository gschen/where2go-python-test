def H(n):
    if n==0 or n==1:
        return n
    else:
        return n*H(n-1)
print(H(5))