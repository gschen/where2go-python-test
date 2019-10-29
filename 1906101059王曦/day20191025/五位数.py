def dao(x):
    list1 = list(x)
    list1.reverse()
    print(list1.__len__())
    for n in list1:
        print(n,end='')


s = str(input('请输入一个小于或等于五位的数：'))
dao(s)