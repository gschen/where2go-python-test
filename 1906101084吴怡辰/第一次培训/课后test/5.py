#5. 现知道有些数为回文数，例如121，242，12321。我们就称这种数字为回文数，像10，14，467就不为回文数。先要求你用程序将区间[1，100000]内所有的回文数输出。
def hws(s):
    return s[::-1] == s

for i in range(10000):
    if (hws(str(i))):
        print(i)