s = str(input('请输入一串数组：'))
list1 = list(s)
list2 =[]
for n in list1:
    list2.append(int(n))
i = eval(input('请输入一个目标数：'))
for x in list2:
    for y in list2:
        if x<y:
            if x + y==i:
                print(list2.index(x),list2.index(y))
