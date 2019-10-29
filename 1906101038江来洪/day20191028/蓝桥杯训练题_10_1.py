#找出100内的素数
list1 = []
list2 = []
for x in range(3,100):
    list1.append(x)
for n in range(3,100):
    for i in range(2,n):
        if n%i == 0:
            list2.append(n)
s = set(list2)
for c in s:
    a = list1.index(c)
    list1.pop(a)
for b in list1:
    print(b,end=',')
