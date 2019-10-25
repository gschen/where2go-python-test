#判断101到200之间有多少个素数并输出
list1 = []
list2 = []
for x in range(101,201):
    list1.append(x)
n = 101
while n<=200:
    for i in range(2,n):
        if n%i == 0:
            list2.append(n)
    n += 1
s = set(list2)
for c in s:
    a = list1.index(c)
    list1.pop(a)
d = len(list1)
print('101到200之间一共有%d个素数，分别是：' % d)
for b in list1:
    print(b,end=',')