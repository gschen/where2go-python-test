# 给你一个整数
# n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。
n = str(input())
list1 = list(n)
a = 1
b = 0
for i in list1:
    a = a*int(i)
    b = b+int(i)
print(a-b)