def L(x):
    return x[::-1]==x
for i in range(100000):
    if(L(str(i))):
        print(i)