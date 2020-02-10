s = map(str,input('请输入一个数组:').split())
list1 = list(s)
list2 =[]
list4 = []
for i in list1:
    list2.append(int(i))
n = list1.__len__()
for a in range(0,n):
    for b in range(0,n):
        for c in range(0,n):
            if a!=c and a!=b and b!=c and list2[a]+list2[b]+list2[c]==0 and list2[a]>=list2[b]>=list2[c]:
                list3 =[[list2[a],list2[b],list2[c]]]
                for i in list3:
                    if i not in list4:
                        list4.append(i)
print(list4)