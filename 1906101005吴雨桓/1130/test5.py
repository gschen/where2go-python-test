def wu(x):
    return x[::-1] == x
for i in range(100000):
    if(wu(str(i))) and i>10:
        print(i)