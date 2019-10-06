a,b = map(int,input().split())
c = 0
s = 0
for i in range(a,b+1):
    s += i
    c += 1
    print("{:>5d}".format(i),end='')
    if c % 5 == 0:
        print('\n',end='')
        c = 0
print('\n',end='')
print('Sum = {}'.format(s))