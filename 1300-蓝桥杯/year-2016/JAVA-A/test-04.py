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


al = perm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
sum = 0
for l in al:
    if l[0] + l[1] != l[2]:
        continue
    if l[3] - l[4] != l[5]:
        continue
    if l[6] * l[7] != l[8]:
        continue
    if l[9] / l[10] != l[11]:
        continue
    sum += 1
print(sum)
