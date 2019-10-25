"""
11、	求1+2!+3!+...+20!的和。
"""

def jiecheng(num):
    if num == 0:
        return "无"
    if num == 1:
        return 1
    if num > 1:
        return num*jiecheng(num-1)


b = int(input("请输入一个数字(大于零)："))
#print(jiecheng(b))
a = 0
for i in range(b):
    a+= jiecheng(b)
    b -=1
