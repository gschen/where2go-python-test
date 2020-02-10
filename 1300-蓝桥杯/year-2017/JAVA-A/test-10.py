
N = int(input())
all = []
allx = []
ally = []
for i in range(N):
    l = list(map(int, input().rstrip().split()))
    allx.extend([l[0], l[2]])
    ally.extend([l[1], l[3]])
    all.append(l)
ap = set()
for one in all:
    for y in range(max(ally)):
        for x in range(max(allx)):
            if one[0] <= x < one[2] and one[1] <= y < one[3]:
                ap.add(str(x) + "," + str(y))
print(len(ap))
