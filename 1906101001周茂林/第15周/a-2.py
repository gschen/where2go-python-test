'''
输入一组M进制的整数，将其转换为L进制后，统计其中的最大值和最小值并输出。
输入说明：第一行是整数N、M和L，N表示这组数的个数，
M表示原始进制（可能是2，5，10），L表示转换后的进制（可能是2，5，10）；第二行是原始进制下的数据（规定输入的数据都是合法的）。
输出说明：转换后的L进制数中的最大值和最小值，中间用空格隔开。
输入样例：6 10 5
         15 9 10 3 6 7
输出样例：30 3
'''
N, M, L = map(int, input().split())
lis = list(map(int, input().split()))
if M != 10:
    for i in range(len(lis)):
        lis[i] = int(lis[i], M)
lis2 = []
for j in lis:
    a = []
    while j != 0:
        s = j // L
        b = j % L
        a.append(b)
        j = s
    a.reverse()
    lis2.append(''.join(str(a)))
print(max(lis2), min(lis2))
