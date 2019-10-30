dict1 = {'li':18,'wang':50,'zhang':20,'sun':22}
dict2 = {x : y for y ,x in dict1.items()}
list1 = list(dict2.keys())
print(dict2[max(list1)])

