x,y = map(int,input().split())
list1 = []
list2 = []
while x >0:
    a,b = map(int,input().split())
    list1.append(a*b)
    x -= 1
s = 0
for i in list1:
    s = s + i
for n in range(1,10000):
    if n*n*y<=s:
        list2.append(n)
print(max(list2))