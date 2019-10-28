#判断一个数是几位数并逆序输出每一位数字
str = str(input('请输入一个数字：'))
a = len(str)
list = []
for i in str:
    list.append(i)
list.reverse()
print('该数是一个%d位数' % a)
for x in list:
    print(x,end='')