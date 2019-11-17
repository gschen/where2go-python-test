n,a,b,r = map(int,input().split(" "))
list1 = []
while n>0:
    x,y =map(int,input().split(" "))
    n -= 1
    list1.append([x,y])
print(list1)
s = 0
for i in list1:
    if (i[0]-a)**2+(i[1]-b)**2<=r**2:
        s +=1
print(s)