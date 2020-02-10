# 4.加法变乘法
# •	我们都知道：1+2+3+ ... + 49 = 1225
# •	现在要求你把其中两个不相邻的加号变成乘号，使得结果为2015
# •	比如：
# •	1+2+3+...+10*11+12+...+27*28+29+...+49 = 2015
# •	就是符合要求的答案。
# •	请你寻找另外一个可能的答案，并把位置靠前的那个乘号左边的数字提交（对于示例，就是提交10）
li=[x for x in range(1,50)]
for a in range(1,len(li)):
    for b in range(a,len(li)-1):
        sums1=sum(range(1,li[a]))
        sums2=sum(range(li[a]+2,li[b]))
        sums3=sum(range(li[b]+2,50))
        x=li[a]*li[a+1]
        y=li[b]*li[b+1]
        if sums1+sums2+sums3+x+y==2015 and li[a]!=10:
            print(li[a])
