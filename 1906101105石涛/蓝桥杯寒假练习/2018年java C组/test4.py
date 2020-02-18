# coding=utf-8

'''
第四题：第几个幸运数
题目描述
到x星球旅行的游客都被发给一个整数，作为游客编号。
x星的国王有个怪癖，他只喜欢数字3,5和7。
国王规定，游客的编号如果只含有因子：3,5,7,就可以获得一份奖品。

我们来看前10个幸运数字是：
3 5 7 9 15 21 25 27 35 45
因而第11个幸运数字是：49

小明领到了一个幸运数字 59084709587505，他去领奖的时候，人家要求他准确地说出这是第几个幸运数字，否则领不到奖品。

请你帮小明计算一下，59084709587505是第几个幸运数字。
(答案：1905)

需要提交的是一个整数，请不要填写任何多余内容。
'''
x=59084709587505
# 这本是想求出它所有的值的，但似乎有点大了，时间上赶不上
# l=[3,5,7]
# li=[3,5,7]
# n=0
# for i in l:
#     for k in li:
#         y=i*k
#         l.append(y)
#     n=len(set(l))
#     if n>=200:
#         l=set(l)
#         l=list(l)
#         l.sort()
#         print(l)
#         print(len(l))
#         break

#换一种思路，看这个数由多少个3，多少个5，多少个7组成
i3,i5,i7=0,0,0
while x/3==x//3:
    x=x/3
    i3+=1
while x/5==x//5:
    x=x/5
    i5+=1
while x/7==x//7:
    x=x/7
    i7+=1
print(i3,i5,i7)
# print(3**i3*5**i5*7**i7)
# print(3**i3*5**i5*7**i7==59084709587505)
i=i3+i5+i7
print(i)    #这里似乎要排下序，又不会了，思路断了




'''这是别人做的'''
# box=[]
# n=59084709587505
# for i in range(1,29):
#     box.append(3**i)
#     box.append(5**i)
#     box.append(7**i)
# for i in range(1,29):
#     for j in range(1,29):
#         box.append(3**i*5**j)
#         box.append(7 **i * 5 ** j)
#         box.append(3 ** i *7 ** j)
# for i in range(1,29):
#     for j in range(1,29):
#         for k in range(1,29):
#             box.append(3**i*5**j*7**k)
# print(sorted(list(set(box))).index(n)+1)