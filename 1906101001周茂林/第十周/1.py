'''
求100之内的素数。（素数：只能被1和本身整除的数）
'''
l = []
for m in range(1,101):
    for n in range(2,m):
        if m % n == 0:
            break
    else:
        l.append(m)
print(l)