# 每一位上的数字都比前一位上的数字大 1 的整数。
# 请你返回由 [low, high] 范围内所有顺次数组成的 有序 列表（从小到大排序）
n = int(input())
m = int(input())
l = []
l2 = []
for i in range(n,m+1):
    l = list(str(i))
    for n in range(len(l)):
        if n+1<len(l):
            if int(l[0])+len(str(n))>len(str(n)):
                if int(l[n+1]) != int(l[n])+1:
                    break
    else:
        l2.append(i)
print(l2)
