#计算1到M 之间的合数数量,输出其值
l = []
m = int(input())
for i in range(1,m+1):
    for n in range(2,m):
        if i%n!=0:
            break
        else:
            l.append(i)
a =len(set(l))
print(a)