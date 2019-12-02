"""
17.对于给出的长度为N的整数数组，对连续3个元素求平方和,输出平方和的最大值。
输入说明:第-行,数组中元素个数N(N< 1000),第二行是这个数组中的N个元素，间用空格隔开,每个元素小于100000.
输出说明:输出连续3个元素平方和的最大值。
输入样例: 8
1 1 -1 2 -3 3 -4 2
输出样例: 34

"""
num = int(input())
a = map(int,input().split())
list1 = []
for i in a:
    list1.append(i)
lenth = len(list1)
list2 = []
for m in range(0,lenth-2):
    sums = list1[m]**2 +list1[m+1]**2 + list1[m+2]**2
    list2.append(sums)
print(max(list2))