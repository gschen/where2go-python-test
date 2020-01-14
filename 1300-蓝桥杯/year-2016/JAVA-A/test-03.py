def perm(l):
    if len(l) <= 1:
        return [l]
    r = []
    for i in range(len(l)):
        s = l[:i] + l[i + 1:]
        p = perm(s)
        for x in p:
            r.append(l[i:i + 1] + x)
    return r


al = []
al.extend(perm([1, 2, 3, 4, 5, 6, 7, 8, 9]))
sum = 0
for a in al:
    if a[0] >= a[2] or a[0] >= a[3]:
        continue
    elif a[1] >= a[3] or a[1] >= a[4]:
        continue
    elif a[2] >= a[5] or a[2] >= a[6]:
        continue
    elif a[3] >= a[6] or a[3] >= a[7]:
        continue
    elif a[4] >= a[7] or a[4] >= a[8]:
        continue
    else:
        sum += 1
print(sum)
