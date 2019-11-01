s = input('请输入一串字符:')
list1 = list(s)
while True:
    if list1[0]!=list1[-1] :
        list1.pop(0)
        if list1[0]!=list1[-1]:
            list1.pop(-1)
    else:
        break
for i in list1:
    print(i,end='')