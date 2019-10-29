#找出年龄最大的人并输出
dict = {'li':18,'wang':50,'zhang':20,'sun':22}
list1 = list(dict.keys())
list2 = list(dict.values())
print(list1[list2.index(max(list2))])