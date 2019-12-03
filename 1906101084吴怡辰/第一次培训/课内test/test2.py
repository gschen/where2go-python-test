def prime(n):
    L=[ ]#设置一个空的列表，方便后面储存得出的结果
    while n>1:#循环得到的所有结果
        for i in range(2,n+1):#for循环的遍历，分解质因数时先考虑在数学中的算法，分析题目，分解为多个不可再分的因数，因为因数的不确定性，要从2开始进行测试知道测试到n

            if n % i==0:
                n = int(n/i)
                L.append(i)
                break
    return L
while 1:
    s = input('请输入一个正整数：')
    if s.isdigit() and int(s)>0:
        print(s,'=','*'.join([str(x) for x in prime(int(s))]))
        #join()方法用于将序列中的元素以指定的字符连接生成一个新的字符串
        #输出语句，[]里面的内容是调用了之前定义的函数prime，用for进行遍历prime函数，再把得到的值用*连接起来
        #*.join(sequence)用*号连接元素序列
