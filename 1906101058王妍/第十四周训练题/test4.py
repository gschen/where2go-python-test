#给定一个正整数N，将其表示为数字1,2,5,11相加的形式输出。

a = int(input())
b = a
l = [11,5,2,1]
l2 = []
for i in l:
    while a >= i:
        a -= i
        l2.append(i)
        l2.append('+')
l2.pop(-1)
print(b,'=',end='')
for c in l2:
    print(c, end='')
