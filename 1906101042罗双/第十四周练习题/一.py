L=[1,1,1,2,3,4,4,4]
for x in range(len(L)-1):
    for y in L[x+1:]:
        if L[x]==y:
            L.remove(L[x])
        else:
            break
print(len(L))
print(L)