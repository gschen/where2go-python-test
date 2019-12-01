# coding=utf-8
'''2 马虎的算式
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
'''
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