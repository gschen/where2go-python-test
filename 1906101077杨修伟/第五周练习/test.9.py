x,y,z=map(int,input().split())
if x==y and x!=z:
    print("C")
if x==z and x!=y:
    print("B")
if y==z and y!=x:
    print("A")