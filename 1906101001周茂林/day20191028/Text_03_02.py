n = int(input())
list4 = []
n2 = 0
for i in range(1,n+1):
    n2 += 1
    a = input()
    a2 = a[:16]
    a3 = 0
    for i in a2:
        if i.isdigit():
            a3 += 1
    if a3 < 16:
        list4.append(a)
        continue
    list1 = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    b = c = 0
    for i in list1:
        b += i
    for m in a2:
        c += int(m)
    z = (b + c) % 11
    list2 = [0,1,2,3,4,5,6,7,8,9,10]
    list3 = ['1','0','x','9','8','7','6','5','4','3','2']
    d = list2.index(z)
    e = list3[d]
    if e != a[17]:
        list4.append(a)
if n2 ==n:
    if len(list4) == 0:
        print('All passed')
    else:
        for i in list4:
            print(i)