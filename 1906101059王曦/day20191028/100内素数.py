l = []
for n in range(101):
    for i in range(2,n):
        if n%i == 0:
            break
    else:
        l.append(n)
else:
    n = 0
print(l)
