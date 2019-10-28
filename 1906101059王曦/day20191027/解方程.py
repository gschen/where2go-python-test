N = eval(input('请输入一个小于或等于10000的数：'))
list1 =[]
list2 =[]
for x in range(1,N+1):
    for y in range(1,N+1):
        s = x**2+y**2
        if s != N:
            n = 1
            list1.append((n))
        else:
            c = 2
            list2.append(c)
            if x <= y:
                print(x,y)
        if x**2>N or y**2>N:
            break
if list1.__len__()!=0 and list2.__len__()==0:
    print('No souition')