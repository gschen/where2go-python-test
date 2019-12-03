x = int(input())
y = x
l = [11,5,2,1]
l2 = []
for n in l:
    while x >= n:
        x -= n
        l2.append(n)
        l2.append('+')
l2.pop(-1)
print(y,'=',end='')
for a in l2:
    print(a,end='')