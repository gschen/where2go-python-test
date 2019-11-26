'''
17.对于给出的长度为N(N< 1000)的正整数数组，满足连续3个元素均为素数的区间称为3素数区间，计算该数组中3素数区间的个数。
输入说明:第一行，数组中元素个数N;第二行，N个正整数,用空格隔开。
输出说明: 3素数区间的个数。
输入样例: 7
3 5 5 7 6 5 8
输出样例: 2
'''
N = int(input())
l = list(map(int,input().split()))
l2 = []
for i in l:
    for j in range(2,i):
        if i%j == 0:
            break
        else:
            l2.append(i)
t = 0
le = len(l)
for k in range(1,le-1):
    if l[k-1] in l2 and l[k] in l2 and l[k+1] in l2:
        t += 1
print(t)

