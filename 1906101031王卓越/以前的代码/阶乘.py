from functools import reduce
def jiec(x,y):
    return x*y
n=list(range(1,101))
k=reduce(jiec,n)
print(k)    