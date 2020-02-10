# coding=utf-8
'''
4.加法变乘法
•	我们都知道：1+2+3+ ... + 49 = 1225
•	现在要求你把其中两个不相邻的加号变成乘号，使得结果为2015
•	比如：
•	1+2+3+...+10*11+12+...+27*28+29+...+49 = 2015
•	就是符合要求的答案。
•	请你寻找另外一个可能的答案，并把位置靠前的那个乘号左边的数字提交（对于示例，就是提交10）。
•	注意：需要你提交的是一个整数，不要填写任何多余的内容。
'''
# (思路：用两个for循环，第一个取前面那个*的值，第二个取后面那个*的值，然后去掉这四个相关的值，再加起来看是否等于2015)
s,n=[],0
for i in range(1,50):
    s.append(i)
sx=s
for it in range(1,48):
    sx.pop(sx.index(it))
    sx.pop(sx.index(it+1))
    for ti in range(it+2,48):
        # print(sx)
        sx.pop(sx.index(ti))
        sx.pop(sx.index(ti+1))
        # print(sx)
        for x in sx:
            n+=x
        # print(n)
        # if it<11:
            # print(it*(it+1)+ti*(ti+1)+n)
        if (it*(it+1)+ti*(ti+1)+n)==2015 and it!=10:
            print(it)
        sx.append(ti)
        sx.append(ti+1)
        sx.sort()
        n=0
    sx.append(it)
    sx.append(it+1)
    sx.sort()
    # print(sx)


'''别人做的'''
# s=[x for x in range(1,50)]
# for i in range(0,46):
#     for j in range(0,48):
#         x=s[i]*s[i+1]
#         y=s[j]*s[j+1]
#         sum_number=x+y+1225-s[i]-s[j]-s[i+1]-s[j+1]
#         if sum_number==2015:
#             print(s[i],s[j])


'''循环节长度
两个整数做除法，有时会产生循环小数，其循环部分称为：循环节。
比如，11/13=6=>0.846153846153.....  其循环节为[846153] 共有6位。
下面的方法，可以求出循环节的长度。
'''