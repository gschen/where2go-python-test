# 第二题：生日蜡烛
# 题目描述
# 某君从某年开始每年都举办一次生日party，并且每次都要吹熄与年龄相同根数的蜡烛。

# 现在算起来，他一共吹熄了236根蜡烛。

# 请问，他从多少岁开始过生日party的？

# 请填写他开始过生日party的年龄数。
# 注意：你提交的应该是一个整数，不要填写任何多余的内容或说明性文字。
def ages(x,sums,start_age):
    sums+=x
    if sums==236:
        return start_age
    if sums>236:
        return ages(start_age+1,0,start_age+1)
    if sums<236:
        return ages(x+1,sums,start_age)
x,sums,start_age=1,0,1
print(ages(x,sums,start_age))
    
