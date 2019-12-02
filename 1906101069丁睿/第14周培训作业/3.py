def my_2(p):
    a=1
    b=2
    c=b/a
    for i in range(0,p-1):
        a,b=b,a+b
        c+=b/a
    return c
print(my_2(20))
