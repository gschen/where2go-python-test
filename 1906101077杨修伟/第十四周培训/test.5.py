L =[]
for n in range(1,100001):
    n = str(n)
    a = len (n)
    if n == n[::-1]:
        print(n)
L.append(n)
print(L)
