'''
对于给出的长度为N(N< 1000)的正整数数组，满足连续3个元素均为素数的区间称为3素数区间，计算该数组中3素数区间的个数。
输入说明:第一行，数组中元素个数N;第二行，N个正整数,用空格隔开。
输出说明: 3素数区间的个数。
输入样例: 7
3 5 5 7 6 5 8
输出样例: 2
'''
def qqqw():
    n = int(input())
    lis = list(map(int,input().split()))
    m = 0
    for i in range(len(lis)-2):
        lis2 = [lis[i],lis[i+1],lis[i+2]]
        for j in lis2:
            if j < 3 or len(lis2) == 0:
                break
            else:
                for q in range(2,j):
                    if j % q == 0:
                        lis2 = []
        if len(lis2) != 0:
            m += 1
    print(m)


qqqw()