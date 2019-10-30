"""
4、	找到年龄最大的人，并输出。字典“{"li":18,"wang":50,"zhang":20,"sun":22}”
"""
dict1 = {"li":18,"wang":50,"zhang":20,"sun":22}
value = list()
for i in dict1.values():
    value.append(i)
# print(sorted(a))      #sorted()可以给列表排序
value = sorted(value)
b = value[3]

value1=list()
for n in  dict1.values():
    value1.append(n)
# print(value1)
weizhi = value1.index(b)

key= list()
for k in dict1:
    key.append(k)
print(key[weizhi]