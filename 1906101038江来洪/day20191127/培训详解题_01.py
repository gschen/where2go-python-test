"""现知道有些数为回文数，例如121，242，12321。
我们就称这种数字为回文数，像10，14，467就不为回文数。
先要求你用程序将区间[1，100000]内所有的回文数输出。
"""
def huiwen(x):                  #定义一个函数，参数为x，就是所求区间的最大值
    for n in range(1,x+1):        #用for循环遍历区间[1，100000]中的每一个数字
        N = str(n)                  #将遍历到的数字n用str函数格式化为可迭代的字符串
        if N == N[::-1]:              #设置条件，原字符串与反向后的字符串是否相等
            print(n)                    #输出满足条件的n
huiwen(100000)                            #调用函数，参数设为所求区间的最大值




