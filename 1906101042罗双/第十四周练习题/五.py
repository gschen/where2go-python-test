def L(x):
    return x[::-1]==x
for n in range(100000):
    if(L(str(n))):
        print(n)