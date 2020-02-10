N, K = map(int, input().split())
ns = []
NS = []
for i in range(N):
    l = list(map(int, input().rstrip().split()))
    ns.append(l)
    NS.extend(l)
m = (min(NS))

for i in range(m, 0, -1):
    k = 0
    for j in ns:
        x = j[0]//i
        y = j[1] // i
        k += x*y
    if k >= 10:
        print(i)
        break
