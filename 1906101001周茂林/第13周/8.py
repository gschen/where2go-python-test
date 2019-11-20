'''
输入一串字符，由字母、数字和空格组成，长度< 1000,判断其中是否存在日期格式的数据。
日期格式的数据具有如下的特征，连续包含年份和月份信息。
年份信息是指连续的四个数字，之后是Jan, Feb, Mar,Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec这些字符串之一.
如” 2019Nov" 就是符合日期格式要求的数据。
输入说明:输入-个字符串。
输出说明:输出包含满足日期格式的字符子串;如果不包含，则输出2000Jan。
输入样例1: Todayis2019Nov15th.
输出样例1: 2019Nov
输入样例2: Todayisasunnyday.
输出样例2: 2000Jan
输入样例3: OnNov05, nothing happen.
输出样例3: 2000Jan
'''
s = input()
L = ['Jan', 'Feb', 'Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
if len(s) <= 7:
    print('2000Jan')
else:
    for i in range(len(s)-3):
        lis = [s[i],s[i+1],s[i+2],s[i+3]]
        for j in lis:
            if not j.isdigit():
                lis = []
    if len(lis) != 0:
        lis2 = [s[i+4],s[i+5],s[i+6]]
        ss = ''.join(lis2)
        if ss in L:
            lis3 = [s[i],s[i+1],s[i+2],s[i+3],s[i+4],s[i+5],s[i+6]]
            print(''.join(lis3))
    else:
        print('2000Jan')
