"""
请写一个函数，函数内部使用迭代查找list中的最大值最小值，返回一个元组
"""
def maxin(x):
    a = list()
    for i in x:
        a.append(ord(i))
        c = int(max(a))
        d = int(min(a))
    return chr(c),chr(d)
f = input()
print(maxin(f))
