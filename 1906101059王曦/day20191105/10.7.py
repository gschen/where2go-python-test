s = input('请输入一串字符:')
list1 = list(s)
list2 = []
list3 = []
for i in range(len(list1)+1):
    for n in range(len(list1)+1):
        if i<n and len(list1[i:n])==len(set(list1[i:n])):
            list2.append(len(list1[i:n]))
            list3.append(list1[i:n])
print(max(list2))
print(list3[list2.index(max(list2))])

