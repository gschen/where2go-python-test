x,y,z = map(int,input().split())
a = min(x,y,z)
b = max(x,y,z)
print(a,x+y+z-a-b,b)