#数列求和加强版
a,b = map(int, input('请分别输入两个值：').split())
n = 1
while n <= b:
    s = a * n
    n += 1
    print(s, end='')