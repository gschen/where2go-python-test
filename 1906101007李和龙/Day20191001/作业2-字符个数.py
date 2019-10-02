m = input("请输入一串字符：")
a = b = c = d = 0
for i in m:
    if ord(i) > 96 and ord(i) < 123 or ord(i) > 64 and ord(i) < 91:
        a += 1
    if ord(i) > 48 and ord(i) < 58:
        b += 1
    if ord(i) == 32:
        c += 1
print("该字符串共有%d个字母，%d个数字，%d个空格"%(a,b,c))