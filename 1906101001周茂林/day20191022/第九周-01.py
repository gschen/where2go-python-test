'''
有四个字母：a、b、c、d，能组成多少个互不相同且无重复三位字符串？输出所有结果。
'''
aa = 'abcd'
for i in aa:
    for m in aa:
        for n in aa:
            if i != m and i != n and m != n:
                print(i,m,n)