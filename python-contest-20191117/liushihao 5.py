import math
a1,a2,a3=map(int,input().split(" "))
b1,b2,b3=map(int,input().split(" "))
t=int(input())
a_val=200
b_val=300
lis=[]
for y1 in range(t//a_val):
    y2=math.ceil((t-a_val*y1)/b_val)
    lis.append([y1,y2])
min_val=float('inf')
for i in range(len(lis)):
    min_new=(a1+a2+a3)*lis[i][0]+(b1+b2+b3)*lis[i][1]
    if min_new <min_val:
        min_val=min_new
print(min_val)
