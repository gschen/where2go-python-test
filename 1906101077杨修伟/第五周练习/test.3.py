a =input()
L = list(a)
a = int(L[0])
b = int(L[1])
c = int(L[2])
if c == 0:
    if b == 0:
        print(a)
    else:
        print("%d%d" % (b,a))
else:
    print("%d%d%d" % (c,b,a))