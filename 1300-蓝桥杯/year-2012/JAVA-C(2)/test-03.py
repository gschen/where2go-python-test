# 3.手机尾号
# 30年的改革开放，给中国带来了翻天覆地的变化。2011全年中国手机产量约为11.72亿部。手机已经成为百姓的基本日用品！
# 给手机选个好听又好记的号码可能是许多人的心愿。但号源有限，只能辅以有偿选号的方法了。
# 这个程序的目的就是：根据给定的手机尾号（4位），按照一定的规则来打分。其规则如下：
# 1. 如果出现连号，不管升序还是降序，都加5分。例如：5678,4321都满足加分标准。
# 2. 前三个数字相同，或后三个数字相同，都加3分。例如：4888,6665,7777都满足加分的标准。注意：7777因为满足这条标准两次，所以这条规则给它加了6分。
# 3. 符合AABB或者ABAB模式的加1分。例如：2255,3939,7777都符合这个模式，所以都被加分。注意：7777因为满足这条标准两次，所以这条标准给它加了2分。
# 4. 含有：6，8，9中任何一个数字，每出现一次加1分。例如4326,6875,9918都符合加分标准。其中，6875被加2分；9918被加3分。
# 尾号最终得分就是每条标准的加分总和！
# 要求程序从标准输入接收数据，在标准输出上输出结果。
# 输入格式为：第一行是一个整数n（<100），表示下边有多少输入行，接下来是n行4位一组的数据，就是等待计算加分的手机尾号。
# 输出格式为：n行整数。


#>>>>>>>>>方法一
def test_1(s:str)->int:
    a = '0123456789'
    if s in a or s[-1::-1] in a:
        return 5
    else:
        return 0
def test_2(s:str)->int:
    l = ['000','111','222','333','444','555','666','777','888','999']
    a = 0
    if s[1:4] in l:
        a += 3
    if s[0:3] in l:
        a+=3
    return a
def test_3(s:str)->int:
    a = 0
    if s[0]==s[1] and s[2]==s[3]:
        a+=1
    if s[0]==s[2] and s[1]==s[3]:
        a+=1
    return a
def test_4(s:str)->int:
    a = 0
    for i in s:
        if i=='6' or i == '8' or i =='9':
            a+=1
    return a
n = int(input())
num_list = []
while n > 0:
    num = input()
    num_list.append(num)
    n -= 1
for i in num_list:
    print(test_4(i)+test_3(i)+test_2(i)+test_1(i),end='\n')



#>>>>>>>>>方法二
#定义判断连号的函数
def lianhao(s):
    sum = 0
    shu1 = shu2 = s[0]
    if int(s[0]) in range(0,7):
        for i in range(3):
            shu1 += str(int(s[i])+1)
    if int(s[0]) in range(3,10):
        for i in range(3):
            shu2 += str(int(s[i])-1)
    if s == shu1 or s == shu2:
        sum += 5
    return sum
#定义前三个数字相同，或后三个数字相同的函数
def ssxt(s):
    sum = 0
    if s[0] == s[1] == s[2]:
        sum += 3
    if s[3] == s[1] == s[2]:
        sum += 3
    return sum
#定义判断符合AABB或者ABAB模式的函数
def lsxt(s):
    sum = 0
    if s[0]==s[1] and s[2] == s[3]:
        sum += 1
    if s[0]==s[2] and s[1] == s[3]:
        sum += 1
    return sum
#定义含有：6，8，9中任何一个数字，每出现一次加1分的函数
def lbj(s):
    sum = 0
    for i in s:
        if int(i)==6 or int(i)==8 or int(i)==9:
            sum+=1
    return sum

n = int(input())
A = []
for i in range(n):
    A.append(input())
for i in A:
    print(lianhao(i)+ssxt(i)+lsxt(i)+lbj(i))
