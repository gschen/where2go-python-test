#求1+2!+3!+...+20!+n!的前n项的和
def jiec(x):
    if x == 0:
        return 1
    elif x != 0:
        return x*(jiec(x-1))
n = int(input('你要求前几项的和：'))
s = 0
for x in range(1,n+1):
    s = s+jiec(x)
print('该式前%d的和为%d' % (n,s))
