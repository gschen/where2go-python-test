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
a=range(1,50)
b=0
for i in range(48):
    n=a[i]*a[i+1]-(a[i]+a[i+1])
    for ii in range(48):
        m=a[ii]*a[ii+1]-(a[ii]+a[ii+1])
        if n+m==2015-1225:
            print(i+1)


'''第二种方法'''
# (思路：这道题之前做过的，这次换个思路，先算1到49的和，然后依然取值，把取到的值减去，加上它们的乘积，看是否等于2015就可以了)
# n=0
# for m in range(1,50):
#     n+=m
# for i in range(1,48):
#     for k in range(i+2,50):
#         x=n-(i+i+1+k+k+1)+k*(k+1)+i*(i+1)
#         if x==2015 and i!=16:
#             print(i)

'''第三种方法
这是我之前做的，比较复杂'''
# (思路：用两个for循环，第一个取前面那个*的值，第二个取后面那个*的值，然后去掉这四个相关的值，再加起来看是否等于2015)
# s,n=[],0
# for i in range(1,50):
#     s.append(i)
# sx=s
# for it in range(1,48):
#     sx.pop(sx.index(it))
#     sx.pop(sx.index(it+1))
#     for ti in range(it+2,48):
#         sx.pop(sx.index(ti))
#         sx.pop(sx.index(ti+1))
#         for x in sx:
#             n+=x
#         if (it*(it+1)+ti*(ti+1)+n)==2015 and it!=10:
#             print(it)
#         sx.append(ti)
#         sx.append(ti+1)
#         sx.sort()
#         n=0
#     sx.append(it)
#     sx.append(it+1)
#     sx.sort()