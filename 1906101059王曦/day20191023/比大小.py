x,y,z=map(int,input().split())
list = [x,y,z]
a = list.index(max(list))
i = max(list)
list.pop(a)
b = list.index(max(list))
n = max(list)
print(list[0],n,i)