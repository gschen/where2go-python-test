ls=[1,1,1,2,3,4,4,4]
for a in range(len(ls)-1):
    for b in ls[a+1:]:
        if ls[a]==b:
            ls.remove(ls[a])
        else:
            break
print(len(ls))
print(ls)