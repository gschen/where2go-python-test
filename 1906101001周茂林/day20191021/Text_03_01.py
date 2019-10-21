sg = list(map(int,input().split()))
n = m = 0
for i in sg:
    n += 1
    m += i
for x in sg:
    if x > m / n:
        print(x,end = " ")
    else:
        continue