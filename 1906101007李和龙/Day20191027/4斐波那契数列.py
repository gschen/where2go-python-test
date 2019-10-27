"""
4、	斐波那契数列。（斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个
数列：0、1、1、2、3、5、8、13、21、34、……。前两项相加等于第三项）
"""

def shulie(n):
    if n<= 2:
        return 1
    else:
        return shulie(n-1) + shulie(n-2)

n = int(input())
print(shulie(n))