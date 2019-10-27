"""
5、	判断101-200之间有多少个素数，并输出所有素数。
"""

a= set()
for i in range (101,200):
    for o in range(2,200):
        if (i%o == 0) and (i != o):
            a.add(i)
b = set()
for m in range(101,200):
    b.add(m)
c = b - a
print(c)
print(len(c))

