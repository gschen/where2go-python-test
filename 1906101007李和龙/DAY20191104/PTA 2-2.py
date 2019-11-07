"""
本题目要求计算下列分段函数f(x)的值：

公式
"""
def hanshu(x):
    if x != 0:
        return 1 / x
    if x == 0:
        return 0
m = int(input())
print("f({})={}".format(m,hanshu(m)))