list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
list3 = []
while len(list3)<len(list1):
    list3 = [list1.index(i) for i in list2]
    list5 = list3[:-1]
    print(list3)
    for c in list3:
        if len(list5)==0:
            list3.insert(c,-(list1[c]))
            list1[c]='a'
        else:
            for a in list5:
                list3.insert(c,c-a-1)
print(list3)