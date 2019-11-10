#去除字符串前后空格
def trim(s):
    list1 = [i for i in s]
    list2 = []
    for n in range(len(list1)):
        if list1[n]!=' ':
            list2.append(n)
    a = min(list2);b = max(list2)
    print(s[a:b])

trim('       oebc voewb vpw        ')
