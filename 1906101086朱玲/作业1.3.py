def f(x):
    if x==1:
        return 2/1
    else:
        return (1/f(x-1) + 1)+f(x-1)
print(f(20))