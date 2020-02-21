# coding=utf-8

'''
第六题：移动距离
题目描述
X星球居民小区的楼房全是一样的，并且按矩阵样式排列。其楼房的编号为1,2,3...
当排满一行时，从下一行相邻的楼往反方向排号。
比如：当小区排号宽度为6时，开始情形如下：

1  2  3  4  5  6
12 11 10 9  8  7
13 14 15 .....

我们的问题是：已知了两个楼号m和n，需要求出它们之间的最短移动距离（不能斜线方向移动）

输出为3个整数w m n，空格分开，都在1到10000范围内,w表示拍号宽度
要求输出一个整数，表示m n 两楼间最短移动距离。

例如：
用户输入：
6 8 2
则，程序应该输出：
4

再例如：
用户输入：
4 7 20
则，程序应该输出：
5
'''
w,n,m=input().split()
if eval(n)%eval(w)==0:
    x1=eval(n)//eval(w)-1
else:
    x1=eval(n)//eval(w)
if eval(m)%eval(w)==0:
    x2=eval(m)//eval(w)-1
else:
    x2=eval(m)//eval(w)
y=abs(x1-x2)
x=abs((eval(n)%eval(w)-1)-((eval(m)//eval(w)+1)*eval(w)-(eval(m)%eval(w)))%eval(w))
# print((eval(n)%eval(w)-1))
# print(((eval(m)//eval(w)+1)*eval(w)-(eval(m)%eval(w)))%eval(w))
# print(y)
# print(x)
len=x+y
print(len)


'''第二种方法'''
# (思路：根据题意，我可以求出这栋楼的横纵坐标，然后再相互相减再相加就得到最短距离了)
# w,m,n=map(int,input().split(' '))
# m1,m2=(m-1)//w+1,m%w
# n1,n2=(n-1)//w+1,n%w
# if m1%2==0:
#     m2=w-m2
# if n1%2==0:
#     n2=w-n2
# print(abs(m1-n1)+abs(m2-n2)+1)