s = map(str,input('请输入一个数组:').split())
list1 = list(s)
list2 = []
#n = list1.__len__()
#list3 = range(n+1)
for i in list1:
    list2.append(int(i))
n = list1.__len__()
for a in range(0,n):
    for b in range(0,n):
        for c in range(0,n):
            if a!=c and a!=b and b!=c and list2[a]+list2[b]+list2[c]==0:

                list3 =[list2[a],list2[b],list2[c]]
                if list3[0]>=list3[1]>=list3[2]:
                    print(list3)