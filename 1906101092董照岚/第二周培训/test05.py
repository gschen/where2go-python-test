#现知道有些数为回文数，例如121，242，12321。我们就称这种数字为回文数，像10，14，467
#就不为回文数。先要求你用程序将区间[1，100000]内所有的回文数输出。

count = 0
for i in range(1,100001):
    a = str(i)
    if str(i) == str(i)[::-1]:
        count += 1
        print(i)
print(count)

for i in range(1,100000):
    if i==int(str(i)[::-1]):#i从前往后读 str（）转换为字符串  int（str（i）[::-1]）:是从后往前读
       print(i)
