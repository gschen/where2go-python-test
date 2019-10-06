x,y=map(int,input().split())
s = 0
for a in range(0, y):
    s =  s+ x * 10 **a
print(s)