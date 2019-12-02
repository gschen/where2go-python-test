#给定一个正整数N，将其表示为数字1,2,5,11相加的形式输出。
x = int(input())
y = x
l = [11,5,2,1]
l2 = []
for i in l:
    while x >= i:
        x -= i
        l2.append(i)
        l2.append('+')
l2.pop(-1)
print(y,'=',end='')
for a in l2:
    print(a,end='')