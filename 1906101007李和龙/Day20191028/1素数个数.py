"""
1、	求100之内的素数。（素数：只能被1和本身整除的数）
"""
a = set()
for i in range(2,101):
    for m in range(2,101):
        if i/m%1 == 0 and i != m:
            a.add(i)
c = set()
for mm in range(2,101):
    c.add(mm)
    d = c - a
print(d)