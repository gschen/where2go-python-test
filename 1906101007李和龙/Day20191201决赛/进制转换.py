N,M,L = map(int,input().split())
num = map(int,input().split())
list1 = []
for i in num:
    if M == 10 :
        if L == 2:
            list1.append(int(bin(i)[2:]))
        if L == 8:
            list1.append(int(oct(i)[2:]))
    if M == 2:
        if L == 10:
            list1.append(int(str(i),2))
        if L == 8:
            list1.append(int(oct(int(str(i),2))[2:]))
    if M == 8:
        if L == 2:
            list1.append(int(bin(i)[2:]))
        if L == 10:
            list1.append(int(int(str(i),8)))
a = max(list1)
b = min(list1)
print(a,b)