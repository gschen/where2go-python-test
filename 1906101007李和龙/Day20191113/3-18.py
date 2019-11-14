"""
随机输入一个字符串，把最左边的10个不重复的英文字母（不区分大小写）挑选出来。 如没有10个英文字母，显示信息“not found”
"""
a=input()
b=a.split()
c=''.join(b)
d=list(set(list(c)))
shu=0
m=0
d.sort(key=c.index)
for i in range(len(d)):
    if 'z' >= d[i] >= 'a' or 'Z' >= d[i] >= 'A' :
        shu=shu+1
if shu<10:          #判断字符个数
    print("not found")
else:
    for i in range(len(d)):
        if m!=10 and 'z'>=d[i]>='a' or 'Z'>=d[i]>='A' :      #这里一定要判断是否为英文字母，题意给出的！
            m=m+1
            print("{}".format(d[i]),end="")


