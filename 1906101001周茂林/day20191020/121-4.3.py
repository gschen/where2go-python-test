a,b = map(int,input().split())
c = a % b
d = a * b
while c != 0:
    a,b = b,c
    c = a % b
print('最大公约数为{},最小公倍数为{:.0f}'.format(b,d/b))