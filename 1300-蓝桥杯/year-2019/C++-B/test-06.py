n = int(input())
list1 = ['2','0','1','9']
list3 = []
for i in range(1,n+1):
    list2 = list(str(i))
    for a in list2:
        if a in list1:
            list3.append(i)
list3 = set(list3)
s = 0
for b in list3:
    s = s + b
print(s)