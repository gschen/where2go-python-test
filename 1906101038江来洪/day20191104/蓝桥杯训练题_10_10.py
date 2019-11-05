#判断输入字符串的括号匹配是否正确
str = input('请输入：')
list1 = []
list2 = ['(',')','[',']','{','}']
list3 = ['(','[','{']
list4 = ['(',')']
list5 = ['[',']']
list6 = []
list7 = []
for i in str:
    if i in list2:
        list1.append(i)
for n in list1:
    if n in list3:
        list6.append(n)
    else:
        if n in list4:
            n = '('
        elif n in list5:
            n = '['
        else:
            n = '{'
        list7.append(n)
s = 0
if len(list6) == len(list7):
    if list6[0] == list7[0]:
        for m in range(len(list6)):
            if list6[m] != list7[m]:
                s += 1
        if s==0:
            print('True')
        else:
            print('False')
    else:
        list6.reverse() and list7.reverse()
        for m in range(len(list6)):
            if list6[m] != list7[m]:
                s += 1
        if s==0:
            print('True')
        else:
            print('False')
else:
    print('False')
