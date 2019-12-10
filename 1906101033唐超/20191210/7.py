'''
给定两个均不超过9的正整数a和n，要求编写程序求a+aa+aaa++⋯+aa⋯a（n个a）之和。
输入格式：
输入在一行中给出不超过9的正整数a和n。
'''





a,n = map(int,input().split())
t = 0
s = 0
b = a
while n>t:
    s += a
    a = a*10+b
    t += 1
print("s=",s)