# 对于给出的长度为N的整数数组，对连续3个元素求平方和,输出平方和的最大值。
# 输入说明:第-行,数组中元素个数N(N< 1000),第二行是这个数组中的N个元素，间用空格隔开,每个元素小于100000.
n = int(input())
s = map(int,input().split())
list1 = list(s)
list3 = []
for i in range(n+1):
    if i+3<=n:
        list2 = list1[i:i+3]
        b = 0
        for a in list2:
            b = a**2+b
            list3.append(b)
print(max(list3))