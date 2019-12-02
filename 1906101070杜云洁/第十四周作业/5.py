def hc(n):
    return n[::-1]==n
for i in range(10000):
    if(hc(str(i))):
        print(i)