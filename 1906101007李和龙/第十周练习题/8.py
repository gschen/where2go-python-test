"""
8、	给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
"""
a = input("给定一个字符串:")
dict1={}
lenth = len(a)
for m in range(lenth+1):
    for n in range(lenth+1):
        if  m < n and a[m:n][::-1] == a[m:n]:
            dict1.update({a[m:n]:len(a[m:n])})
    # print(dict1)
    # for value in dict1.values():
    #     for key in dict1.keys():
    #      value1= max(list(value))
    #      print(value)
    #         print(value)
    #         print(key)
aa= max(dict1.values())
    # print(aa)
for key,value in dict1.items():
    if value == aa:
        print(key)
# print(hui("abcddcbaffffffbffffff"))