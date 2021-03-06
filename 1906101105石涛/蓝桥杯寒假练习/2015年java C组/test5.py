# coding=utf-8

'''
第五题：加法变乘法
题目描述
我们都知道：1+2+3+ ... + 49 = 1225
现在要求你把其中两个不相邻的加号变成乘号，使得结果为2015

比如：
1+2+3+...+10*11+12+...+27*28+29+...+49 = 2015
就是符合要求的答案。

请你寻找另外一个可能的答案，并把位置靠前的那个乘号左边的数字提交（对于示例，就是提交10）。

注意：需要你提交的是一个整数，不要填写任何多余的内容。

'''
# (思路：这道题之前做过的，这次换个思路，先算1到49的和，然后依然取值，把取到的值减去，加上它们的乘积，看是否等于2015就可以了)
n=0
for m in range(1,50):
    n+=m
for i in range(1,48):
    for k in range(i+2,50):
        x=n-(i+i+1+k+k+1)+k*(k+1)+i*(i+1)
        if x==2015 and i!=16:
            print(i)