#判断输入数字范围内有多少个合数
M = int(input())
s = 0
for i in range(1,M+1):
    for n in range(2,i):
        if i%n == 0:
            s+=1
            break
print(s)