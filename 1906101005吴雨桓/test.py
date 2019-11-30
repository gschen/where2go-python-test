l1 = [1,1,1,2,3,4,4,4]
l2 = []
for i in l1:
    if not i in l2:
        l2.append(i)
print(len(l2))
print(l2)