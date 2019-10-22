sr = input()
a = b = c = d = 0
for e in sr:
    if e.isalpha():
        a += 1
    elif e.isdigit():
        b += 1
    elif e.isspace():
        c += 1
    else:
        d += 1
print('经统计:中英文字母{}个,数字{}个,空格{}个,其他字符{}个'.format(a,b,c,d))