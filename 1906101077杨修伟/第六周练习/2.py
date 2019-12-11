n,u,d=map(int,input().split())
t = 0
s = 0
while s <n:
    s = s+u
    t = t+1
    if s >= n:
        print(t)
        break
    t = t+1
    s = s-d
else:
    print(t)