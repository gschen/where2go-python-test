#找到给定字符串中最长的回文子串
def daoxu(x):
    list = []
    for i in x:
        list.append(i)
    list.reverse()
    return (''.join(list))
str = input('请输入一个字符串：')
list1 = []
for m in range(len(str)+1):
    for n in range(len(str)+1):
        x = str[m:n]
        if x == daoxu(x):
            list1.append(x)
print(max(list1))
