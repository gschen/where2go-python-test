'''
判断输入的字符串中是否含有日期信息，满足条件的日期信息是指:
年份在1979到2019之间，月份表达为01到12,且年份信息和月份信息之间用’- '连接
如”2010-06"就是满足条件的日期信息。如果找到这样的日期信息，请输出该信息在字符串中的位置，
即年份信息的第一个字符在字符串中出现的位置,如果有多个满足条件的日期信息,仅输出第-一个
如果字符串中不包含有效日期信息，请输出-1。说明，输入字符串的第一个元素的位置是1。
输入说明:输入一个字符串。
输出说明:满足条件的日期信息出现的位置。
输入样例: 2011Dec1119921 5072019-1216
输出样例: 18
'''
s = list(input())
for i in s:
    if i == ' ':
        s.remove(i)
for i in range(len(s)):
    if s[i].isdigit() and s[i+1].isdigit() and s[i+2].isdigit() \
            and s[i+3].isdigit() and s[i+5].isdigit() and s[i+6].isdigit():
        if 1979 <= int(s[i]+s[i+1]+s[i+2]+s[i+3]) <= 2019 \
                and s[i+4] == '-' and 1 <= int(s[i+5]+s[i+6]) <= 12:
            print(i+1)
            s = []
            break
if len(s) != 0:
    print('-1')
