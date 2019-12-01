'''
给定K个整数组成的序列{ N1, N2, ..., NK}，“连续子列”被定义为{ Ni, Ni+1​, ..., Nj}，其中 1≤i≤j≤K。“最大子列和”则被定义为所有连续子列元素的和中最大者。例如给定序列{ -2, 11, -4, 13, -5, -2 }，其连续子列{ 11, -4, 13 }有最大的和20。现要求你编写程序，计算给定整数序列的最大子列和。
本题旨在测试各种不同的算法在各种数据情况下的表现。各组测试数据特点如下：
数据1：与样例等价，测试基本正确性；
数据2：10**2个随机整数；
数据3：10**3个随机整数；
数据4：10**4个随机整数；
数据5：10**5个随机整数；
输入样例:
6
-2 11 -4 13 -5 -2
输出样例:
20
'''
n = int(input())
l = []
while n > 0:
    n -= 1
    m = int(input())
    l.append(m)
k = len(l)
L = []
for i in range(k):
    for j in range(i,k):
        a = sum(l[i:j+1])
        L.append(a)
print(max(L))


n = int(input())
l = list(map(int,input().split()))
l2 = []
for i in range(0,n):
    for j in range(1,n):
        if i < j:
            l2.append(sum(l[i:j+1]))
print(max(l2))