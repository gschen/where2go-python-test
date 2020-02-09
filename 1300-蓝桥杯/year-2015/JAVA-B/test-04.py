# coding=utf-8

'''循环节长度
两个整数做除法，有时会产生循环小数，其循环部分称为：循环节。
比如，11/13=6=>0.846153846153.....  其循环节为[846153] 共有6位。
下面的方法，可以求出循环节的长度。
'''
a,b=map(int,input().split('/'))
s=str(a/b)
x=False
for j in range(2,len(s)):
    for i in range(1,b+1):
        if s[j:j+i]==s[j+i:j+2*i]:
            x=True
            print(i)
            break
    if x==True:
        break



#不一样的另外一个2015年java B组的题
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