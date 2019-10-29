#输入的奇数和偶数调用不同的函数
def jiang(n):
    s = 0
    x = 2
    y = 1
    if n%2 == 0:
        while x<=n:
            s = s+1/x
            x += 2
        return s
    else:
        while y<=n:
            s = s+1/y
            y += 2
        return s
n = int(input('请输入一个数：'))
print(jiang(n))