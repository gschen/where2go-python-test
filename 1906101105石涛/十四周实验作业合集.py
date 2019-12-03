# coding=utf-8

# 第一题
print()
print('欢迎来到第一题')
print()
L=[]
l=set([1,1,1,2,3,4,4,4])
print(l)
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