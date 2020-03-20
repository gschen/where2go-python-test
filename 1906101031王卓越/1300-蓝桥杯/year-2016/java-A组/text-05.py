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
class Methed():
    def main(self,nums):
        if nums ==5:
            self.pos=[-4,4,1]
        if nums in [2,3]:
            self.pos=[4,-1,1]          
        if nums ==8:
            self.pos=[-4,4,-1]
        if nums in [10,11]:
            self.pos=[-4,-1,1]
        if nums==1:
            self.pos=[4,1]
        if nums==9:
            self.pos=[-4,1]
        if nums==4:
            self.pos=[-1,4]
        if nums==12:
            self.pos=[-4,-1]
        if nums in [6,7]:
            self.pos=[-4,4,-1,1]
    def operation(self,x):
        if x==12:
            return self.pos
        return Methed(x)
for x in range(1,13):
    md= Methed(x)
    print(md.operation(x))

