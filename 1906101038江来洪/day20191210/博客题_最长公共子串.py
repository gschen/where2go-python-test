N = int(input())                #输入一个整数，代表你下面要输的行数
lis = []
lis1 = []                       #定义两个空列表备用
for i in range(N):
    ss = input()                #输入需要比较的字符串
    lis.append(ss)              #将输入的每行字符串加入列表lis
ss1 = lis[0]
for a in lis:
    if len(a)<len(ss1):
        ss1 = a             #用for循环找出列表lis中最短字符串，并求其长度，然后从列表lis中删除
l = len(ss1)
lis.remove(ss1)
num2 = 0                        #定义一个计数变量
for n in range(l):                  #以最短字符串长度来定循环次数，遍历每一种子字符串长度的情况
    for b in range(n+1):            #遍历一种长度的每一种子字符串
        num1 = 0
        for m in lis:                   #遍历lis中的每一个字符串
            if ss1[b:l-n+b] in m and ss1[b:l-n+b] not in lis1:      #用切片依次切出一种长度的每种子字符串
                num1 += 1           #若该子字符串在字符串m中，并且不与前面切出过的子字符串相同计数器就加1
        if num1 == N-1:             #如果计数器的值与lis的长度及N-1相等，说明该子字符串在lis的每一个字符串中
            num2 = 1                #找到一个最长公共子字符串计数器num2就等于1
            lis1.append(ss1[b:l-n+b])       #满足的条件的子字符串加到列表lis1中
            print(ss1[b:l-n+b],end=' ')     #输出所有相同长度且都为最长公共子字符串的子字符串
    if num2 == 1:
        break       #如果循环完一种长度的所有种子字符串且找到了最长公共子字符串，循环终止
