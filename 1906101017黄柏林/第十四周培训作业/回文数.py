'''
# 现知道有些数为回文数，例如121，242，12321。
# 我们就称这种数字为回文数，像10，14，467就不为回文数。先要求你用程序将区间[1，100000]内所有的回文数输出。
'''
L=list(range(1,100000))
for i in L:
    i=str(i)
    if i==i[::-1]:
        print(i)