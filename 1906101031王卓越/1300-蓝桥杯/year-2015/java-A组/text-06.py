# X星球居民小区的楼房全是一样的，并且按矩阵样式排列。其楼房的编号为1,2,3...
# 当排满一行时，从下一行相邻的楼往反方向排号。
# 比如：当小区排号宽度为6时，开始情形如下：
# 1 2 3 4 5 6
# 12 11 10 9 8 7
# 13 14 15 .....
# 我们的问题是：已知了两个楼号m和n，需要求出它们之间的最短移动距离（不能斜线方向移动）
# 输入为3个整数w m n，空格分开，都在1到10000范围内
# w为排号宽度，m,n为待计算的楼号。
# 要求输出一个整数，表示m n 两楼间最短移动距离。
# 例如：
# 用户输入：
# 6 8 2
# 则，程序应该输出：
# 4
# 再例如：
# 用户输入：
# 4 7 20
# 则，程序应该输出：
# 5
# 资源约定：
# 峰值内存消耗（含虚拟机） < 256M
# CPU消耗 < 1000ms
w,m,n=map(int,input().split(' '))
a=max(m,n)//w
a1=max(m%w,n%w)
b=min(m,n)//w
b1=min(m%w,n%w)
if m%w==0 and n%w!=0 or m%w!=0 and n%w==0:
    a-=1
if a%2==b%2 and  m%w!=0 and n%w!=0 or a%2!=b%2 and m%w==0 or a%2!=b%2 and n%w==0:
    if a%2!=b%2 and m%w==0 and n%w==0:
        print(a-b+w-1)
    if a%2!=b%2 and m%w==0 and n%w!=0 or a%2!=b%2 and n%w==0 and m%w!=0:
        print(a1+a-b-1)
    if m%w!=0 and n%w!=0:
        print(a1-b1+a-b)
if a%2!=b%2 and  m%w!=0 and n%w!=0 or a%2==b%2 and m%w==0 or a%2==b%2 and n%w==0:
    if a%2==b%2 and  m%w==0 and n%w==0:
        print(a-b)
    if a%2==b%2 and m%w==0 and n%w!=0 or  a%2==b%2 and n%w==0 and m%w!=0:
        print(w-a1+a-b)
    if m%w!=0 and n%w!=0:
        print(w+1-a1-b1+a-b)
