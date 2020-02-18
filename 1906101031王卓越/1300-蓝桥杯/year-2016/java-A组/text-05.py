# 第五题：剪邮票
# 题目描述
# 如【图1.jpg】, 有12张连在一起的12生肖的邮票。
# 现在你要从中剪下5张来，要求必须是连着的。
# （仅仅连接一个角不算相连）
# 比如，【图2.jpg】，【图3.jpg】中，粉红色所示部分就是合格的剪取。

# 请你计算，一共有多少种不同的剪取方法。

# 请填写表示方案数目的整数。
# 注意：你提交的应该是一个整数，不要填写任何多余的内容或说明性文字。


# 图1.jpg
 
# 图2.jpg

# 图3.jpg
pos=[-4,4,-1,1]
sum=0
def judge(nums):
    if nums ==5:
        pos=[-4,4,1]
        return pos
    if nums in [2,3]:
        pos=[4,-1,1]
        return pos
    if nums ==8:
        pos=[-4,4,-1]
        return pos
    if nums in [10,11]:
        pos=[-4,-1,1]
        return pos
    if nums==1:
        pos=[4,1]
        return pos
    if nums==9:
        pos=[-4,1]
        return pos
    if nums==4:
        pos=[-1,4]
        return pos
    if nums==12:
        pos=[-4,-1]
        return pos
    if nums in [6,7]:
        pos=[-4,4,-1,1]
        return pos
for num in range(1,13):
    nums=num
    pos=judge(nums)
    for i in pos:
        num=num+i
        pos=judge(nums)
        for i in pos:
            num=num+i
            pos=judge(nums)
            for i in pos:
                num=num+i
                pos=judge(nums)
                for i in pos:
                    num=num+i
                    print(nums)
                    
                    sum+=1
print(sum) 

