#求11+12+13+。。。+m
m = int(input('请输入一个数：'))
S = m
for x in range(11,m):
    S = S+x
print('sum =',S)