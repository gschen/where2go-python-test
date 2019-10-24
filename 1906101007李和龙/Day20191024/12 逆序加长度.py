"""
12、	给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
"""

a = int(input("请输入一个不多于5位的正整数："))
#a = str(a)
lenth = len(str(a))       #  求字符串长度
print("这个数是%d位数"%lenth)
print("逆序打印为：")
while lenth != 0:
    print(str(a)[lenth-1],end="")      #通过将输入整数变为字符串，通过长度的数字用while来反向输出
    lenth -= 1