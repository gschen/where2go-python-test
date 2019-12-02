import math
a1,b1,c1 = map(int,input().split(" "))
a2,b2,c2 = map(int,input().split(" "))
a0,b0,c0 = map(int,input().split(" "))
li=[]
for x in range(a0//a1):
    for y in range(a0 // a2 - x):
        li.append([x, y])
min_val = float('inf')
for i in range(len(li)):
    min_new=a0+b0+c0-li[i][0]*(a1+b1+c1)-li[i][1]*(a2+b2+c2)
    if min_new <min_val:
        min_val=min_new
print(min_val)

















