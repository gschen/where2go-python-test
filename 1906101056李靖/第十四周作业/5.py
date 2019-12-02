#现知道有些数为回文数，例如121，242，12321。我们就称这种数字为回文数，先要求你用程序将区间[1，100000]内所有的回文数输出。
def zheng(x):
    return x[::-1]==x
for i in range(100000):
    if(zheng(str(i))):
        print(i)