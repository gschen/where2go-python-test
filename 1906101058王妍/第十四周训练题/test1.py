Ls=[1,1,1,2,3,4,4,4]
for x in range(len(Ls)-1):
    for y in Ls[x+1: ]:
        if Ls[x] == y:
            Ls.remove(Ls[x])
        else:
            break
print(len(Ls))
print(Ls)
