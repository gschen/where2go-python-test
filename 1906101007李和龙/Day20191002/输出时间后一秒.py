timee = input("请输入时间：")
a = timee.split(":")
b = int(a[0])
c = int(a[1])
d = int(a[2])
d += 1
if d == 60:
    c += 1
    d = 0
    if c == 60:
        b += 1
        c = 0
        if b == 24:
            b = 0
print("下一秒为：%.2d:%.2d:%.2d"% (b,c,d))