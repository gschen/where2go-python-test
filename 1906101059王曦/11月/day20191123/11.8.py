# 输入一串字符，由字母、数字和空格组成，长度< 1000,判断其中是否存在日期格式的数据。
# 日期格式的数据具有如下的特征，连续包含年份和月份信息
list1 = ['Jan', 'Feb', 'Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
list3 = ['0','1','2','3','4','5','6','7','8','9']
s = str(input())
for n in range(len(s)):
    for i in list1:
        if i in s[n:n+3]:
            list2 = s[n-4:n]
            a = 0
            for d in list2:
                if d in list3:
                    a+=1
            if a == 4:
                m = 0
                print(list2+s[n:n+3])
                if m != 0:
                    print('2000Jan')