# 给你一个整数 n，请你返回 任意 一个由 n 个 各不相同 的整数组成的数组，
# 并且这 n 个数相加和为 0 。
n = int(input())
list1 = []
if n % 2 == 0:
    for i in range(1,(int((n+1)/2))+1):
        list1.append(i)
        list1.append(-i)
elif n == 1:
    list1.append(0)
else:
    s = n+1
    for i in range(int((s+1)/2)):
        list1.append(i)
        list1.append(-i)
    list1.remove(0)
print(list1)