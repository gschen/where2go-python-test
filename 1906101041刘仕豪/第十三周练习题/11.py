'''
18.给出一一个字符串(长度< 10000),统计其中四个字母(b、 m、p、t) 出现的次数,并按出现次数降序输出字母和该字母的出现次数(不区分大小写)，如果两个字母的出现次数一样，则按照字母升序输出。
输入说明:一个字符串。
输出说明:分4行输出，每个字母一行。 格式为字母和出现次数，以单个空格分隔。
输入样例: 123aabapsobwo
输出样例: b 2
P 1
m 0
t 0
'''
s = input()
l = ['b','m','p','t']
for j in range(0,len(l)):
    for k in range(len(l)):
        if s.count(l[j]) > s.count(l[k]):
            l[j],l[k] = l[k],l[j]
for i in l:
    print('{} {}'.format(i,s.count(i)))