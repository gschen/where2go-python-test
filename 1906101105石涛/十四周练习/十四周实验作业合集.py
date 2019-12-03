# coding=utf-8
'''
1给定一个数组，你需要删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度和新的数组
输入样例：[1,1,1,2,3,4,4,4]
输出样式：4        [1,2,3,4]


2 马虎的算式
小明是个急性子，上小学的时候经常把老师写在黑板上的题目抄错了。
有一次，老师出的题目是：36 x 495 = ?
他却给抄成了：396 x 45 = ?
但结果却很戏剧性，他的答案竟然是对的！！
假设 a b c d e 代表1~9不同的5个数字（注意是各不相同的数字，且不含0）
能满足形如： ab * cde = adb * ce 这样的算式一共有多少种呢？
请你利用计算机的优势寻找所有的可能，并回答不同算式的种类数。
满足乘法交换律的算式计为不同的种类，所以答案肯定是个偶数。
因为 36 * 495 = 396 * 45 = 17820
类似这样的巧合情况可能还有很多，比如：27 * 594 = 297 * 54
思路：循环遍历。
答案：142


3. 有一分数序列:2/1,3/2,5/3,8/5,13/8,21/13 求出这个数列的前20项之和
提示：用递归


4. 给定一个正整数N，将其表示为数字1,2,5,11相加的形式输出。 要求上述数字出现的总次数最少(每个数字可以重复使用)。
输入说明:一个正整数N (N<= 10000)。
输入：21
输出：11
	   5
	   5


5. 现知道有些数为回文数，例如121，242，12321。我们就称这种数字为回文数，像10，14，467就不为回文数。先要求你用程序将区间[1，100000]内所有的回文数输出。
'''
# 第一题
print()
print('欢迎来到第一题')
print()
L=[]
l=set([1,1,1,2,3,4,4,4])
# print(l)
for i in l:
    # print(i)
    L.append(i)
print('列表的元素个数为:',len(L),'列表为:',L)

#第二题
print()
print('欢迎来到第二题')
print()
#这段为测试
# a,b,c,d,e=1,2,3,4,5
# l=set([a*10+b,c*100+d*10+e,a*100+d*10+b,c*10+e])
# print(l)
# L.append(l)
# print(L)
# print(len(L))

L=[]
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                for e in range(1,10):
                    if a!=b and a!=c and a!=d and a!=e and b!=c and b!=d and b!=e and c!=d and c!=e and d!=e:
                        if (a*10+b)*(c*100+d*10+e)==(a*100+d*10+b)*(c*10+e):
                            l=[a*10+b,c*100+d*10+e,a*100+d*10+b,c*10+e]
                            for i in l:
                                L.append(i)
m=len(L)/4
print('如此计算能有的种类数：%0.f' %m)

#第三题
print()
print('欢迎来到第三题')
print()
# 2/1,3/2,5/3,8/5,13/8,21/13...
#2,3,5,8,13,21,33,54...
#1,2,3,5,8,13,,21,33...

#分子
def y(n):
    a,b=1,2
    while n>0:
        a,b=b,a+b
        n=n-1
    return a
print('第20个分子是：',y(20))
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
        return (y(x)/k(x)+f(x-1))
print(f(20))

#第四题
print()
print('欢迎来到第四题')
print()
#1,2,5,11
x=int(input('请输入一个你比较喜欢的正整数：'))
print()
print('准备好了吗？我要开拆了哈，嘿嘿...')
while x>=11:
    x=x-11
    print(11)
while x>=5:
    x=x-5
    print(5)
while x>=2:
    x=x-2
    print(2)
if x==1:
    print(1)

#第五题
print()
print('欢迎来到第五题')
print()
l=[]
L=[]
for i in range(1,100000):
    l.append([str(i)])
# print(l)
for i in l:
    # x=len([x for x in str(' '.join(i))])
    # print(x)
    for ii in i[0][0]:
        # print(ii)
        for iii in i[0][-1]:
            # print(iii)
            if ii==iii and len([x for x in str(' '.join(i))])<=2:
                L.append(i)
            elif ii==iii and len([x for x in str(' '.join(i))])>=3:
                for m in [i]:
                    for mm in m[0][1]:
                        for mmm in m[0][-2]:
                            if mm==mmm and len([x for x in str(' '.join(m))])<=5:
                                L.append(m)
                            elif mm==mmm and len([x for x in str(' '.join(m))])>=6:
                                for n in [m]:
                                    for nn in m[0][2]:
                                        for nnn in m[0][-3]:
                                            if nn==nnn:
                                                L.append(n)
print('以下是100000内所有的回文数：')
print()
print(L)