'''我们都知道：1+2+3+ ... + 49 = 1225
现在要求你把其中两个不相邻的加号变成乘号，使得结果为2015
比如：
1+2+3+...+10*11+12+...+27*28+29+...+49 = 2015
就是符合要求的答案。
请你寻找另外一个可能的答案，并把位置靠前的那个乘号左边的数字提交（对于示例，就是提交10）
注意：需要你提交的是一个整数，不要填写任何多余的内容
'''
for i in range(1,48):
    for j in range(i+2,50):
        sum=0
        for x in range(1,50):
            if x==i or x==j:
                sum*=x
                if x==i:
                    t=x
            else:
                sum+=x
        print(sum)
        if sum==2015:
            print(t)