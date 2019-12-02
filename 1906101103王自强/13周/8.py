'''18.输入一串字符,由字母、数字和空格组成，长度< 1000,判断其中是否存在日期格式的数据。日期格式
的数据具有如下的特征，连续包含年份和月份信息。年份信息是指连续的四个数字,之后是Jan, Feb, Mar,
Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec这些字符串之一-,如” 2019Nov" 就是符合日期格式要求的
数据。.
输入说明:输入一个字符串。
输出说明:输出包含满足日期格式的字符子串;如果不包含,则输出2000Jan。
输入样例1: Todayis2019Nov15th.
输出样例1: 2019Nov
输入样例2: Todayisasunnyday.
输出样例2: 2000Jan
输入样例3: OnNov05, nothing happen.
输出样例3: 2000Jan
代码提交说明:
1.请严格按照每道题目给出的输入/输出样例编写相关I/O代码,数字间的默认间隔是一个空格， 浮点数的默认输出精度是保持
小数点后2位。样例以外的提示信息请不要在屏幕上输出。
2.请大家确保提交的代码可以在指定的编译条件下正确地编译执行，否则自动评测程序将给出编译错误或运行时错误的信息。
3.每道编程题目，如果没有特殊说明，需要在1秒内完成程序的运行和输出结果，超过这个时间限制将会被判超时,失去相应
测试用例的分数。每个可执行文件可使用的空间不得大于1MB。
4.每道编程题会有多个测试用例，每通过一些测试用例可以获得相应的分值，但只有通过全部测试用例才能拿到这题全部的分
数。
'''
a=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
s=input()
l=len(s)
box=[]
if l>7:
    for i in range(5,l):
        if s[i-1:i+2]in a:
            box.append(i)
    if box==[]:
        print('2000Jan')
    else:
        for j in box:
            if (s[j-5:j-1]).isdigit()==True:
                print(s[j-5:j+2])
            else:
                print('2000Jan')
else:
