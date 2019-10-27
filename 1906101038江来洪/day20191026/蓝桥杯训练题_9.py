#找出三队赛手的名单
list1 = []
list2 = []
for m in range(ord('a'),ord('d')):
    for n in range(ord('x'),ord('z')+1):
        if m+23 != n and m+24 != n and m+21 != n:
            list1.append(chr(m))
            list2.append(chr(n))
n = 0
while n <= 2:
    j = list1[n]
    k = list2[n]
    print('%s VS %s' % (j,k),end='; ')
    n += 1