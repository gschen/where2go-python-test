# 字母连连看,给定一个由小写英文字母组成的字符串(长度 <1000),
# 如果字符串中有两个连续的字母相同，则这两个字母可同时消除，
# 并不断重复该操作，直到不能消除为止
list1 = [i for i in str(input())]
n = len(list1)
while n>1:
    for i in range(len(list1)):
        if i+1<len(list1):
            if list1[i]==list1[i+1]:
                list1.pop(i)
                list1.pop(i)
    n -= 1
if len(list1)==0:
    print('yes')
else:
    for d in list1:
        print(d,end='')