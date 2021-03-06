'''
如果把一个正整数的每一位都平方后再求和，得到一个新的正整数。
对新产生的正整数再做同样的处理。
如此一来，你会发现，不管开始取的是什么数字，
最终如果不是落入1，就是落入同一个循环圈。
请写出这个循环圈中最大的那个数字。
请填写该最大数字。
'''
a = int(input())    #输入一个正整数
lis = []            #创立一个空列表
while len(set(lis)) == len(lis):
    a, b = 0, a     #a恢复为0，便于储存平方和；并且a赋值给b，使其进行下一次循环
    for i in list(str(b)):
        a += int(i)**2
    lis.append(a)
print(max(lis))

