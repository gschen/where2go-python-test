#  第四题：奇妙的数字
# 题目描述
# 小明发现了一个奇妙的数字。它的平方和立方正好把0~9的10个数字每个用且只用了一次。
# 你能猜出这个数字是多少吗？

# 请填写该数字，不要填写任何多余的内容。
num=0
for x in range(0,250):
    if len(set(list(str(x**2))))==len(list(str(x**2)))==4 and len(set(list(str(x**3))))==len(list(str(x**3)))==6 :
        for a in list(str(x**2)):
            if a not in list(str(x**3)):
                num+=1
                if num==4:
                    print(x)  
            else:
                break

