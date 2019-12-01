# coding=utf-8
'''3. 有一分数序列:2/1,3/2,5/3,8/5,13/8,21/13 求出这个数列的前20项之和
提示：用递归'''
# 2/1,3/2,5/3,8/5,13/8,21/13...
#2,3,5,8,13,21,33,54...
#1,2,3,5,8,13,,21,33...

#分子
def m(n):
    a,b=1,2
    while n>0:
        a,b=b,a+b
        n=n-1
    return a
print('第20个分子是：',m(20))
#分母
def k(n):
    a,b=1,1
    while n>0:
        a,b=b,a+b
        n=n-1
    return a
print('第20个分母是：',k(20))
#各项和
def f(x):
    if x==1:
        return 2/1
    else:
        return (m(x)/k(x)+f(x-1))
print(f(20))