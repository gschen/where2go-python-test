'''对于给出的长度为N(N< 1000)的正整数数组，满足连续3个元素均为素数的区间称为3素数区间，计算该数组中3素数区间的个数。
输入说明:第一行，数组中元素个数N;第二行，N个正整数,用空格隔开。
输出说明: 3素数区间的个数。
输入样例: 7
3 5 5 7 6 5 8
输出样例: 2'''
N=int(input())
l=list(input().split(' '))
def isheshu(x):
    a=False
    for i in range(2,x):
        if x%i==0:
            a=True
            break
    return a
b=0
for i in range(N-2):
    if isheshu(int(l[i]))==False and isheshu(int(l[i+1]))==False and isheshu(int(l[i+2]))==False:
        b+=1
print(b)