def jc(x):
    if x==1:
        return(x)
    return x*jc(x-1)
print(jc(5))
