def jc(x):
    if x==1:
        return x
    else:
        return x*jc(x-1)
print(jc(5))
