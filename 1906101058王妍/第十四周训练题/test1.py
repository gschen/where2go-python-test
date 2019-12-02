l=[1,1,1,2,3,4,4,4]
for x in range(len(l)-1):
    for y in l[x+1: ]:
        if l[x] == y:
            l.remove(l[x])
        else:
            break
print(len(l))
print(l)
