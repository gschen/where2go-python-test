"""
10、	有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
"""
a = 2
b = 1
c = int(input("请输入多少项："))
sum = 0
for i in range(c):
    sum = a / b + sum
    a,b = (a + b),a

print(sum)