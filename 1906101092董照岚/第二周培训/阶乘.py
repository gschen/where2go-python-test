
def jc(n):
    if n==1:
        return 1
    else:
        return n*jc(n-1)
print(jc(4))

