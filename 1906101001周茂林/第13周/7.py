'''
给定一个正整数N，将其表示为数字1,2,5,11相加的形式输出。 要求上述数字出现的总次数最少(每个数字可以重复使用)。
输入说明:一个正整数N (N<= 10000)。
输出说明:正整数N由1,2,5,11组成的加法表达式，要求非递增排列。
输入样例: 21
输出样例: 21=11+5+5
'''
N = int(input())
n = N
lis = [11,5,2,1]
lis2 = []
for i in lis:
    while N >= i:
        N -= i
        lis2.append(i)
        lis2.append('+')
lis2.pop(-1)
print(n,'=',end=' ')
for k in lis2:
    print(k,end=' ')

