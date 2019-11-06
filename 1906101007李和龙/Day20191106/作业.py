"""
实现addMulti()函数，参数个数不限，返回所有参数的平方和
"""


def addMulti(*nums):
    a = list()
    for i in nums:
        i = int(i)
        x = i ** 2
        a.append(x)
        v = sum(a)
    return v


L = list()
c = input("请输入多个数字，以空格分开：")
for mm in c.split():
    L.append(mm)
print(addMulti(*L))




