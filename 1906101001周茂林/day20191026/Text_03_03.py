a = list(input())
c,d = input().split()
b = len(a)
n = m = b
for i in a[::-1]:
    n -= 1
    if i == d:
        print(n,i)
for i in a[::-1]:
    m -= 1
    if i == c:
        print(m,i)