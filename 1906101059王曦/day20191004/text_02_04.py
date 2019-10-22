x,y=map(int,input().split())
s = 0
c = 0
if y>=0:
    for a in range(0,y):
        s = s+x+x*10**a
    c = s+c
    y = y-1
print(c)


