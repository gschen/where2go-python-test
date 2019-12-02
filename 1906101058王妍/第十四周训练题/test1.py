ls=[1,1,1,2,3,4,4,4]
for x in range(len(ls)-1):
    for y in Ls[x+1: ]:
        if ls[x] == y:
            ls.remove(ls[x])
        else:
            break
print(len(ls))
print(ls)
