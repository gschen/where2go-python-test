"""
请写一个函数，利用切片实现对字符串的首尾空格删除，不能利用str的strip（）函数
"""

def shan(x):
    lenth = len(x)
    if lenth > 0:
        for i in range(lenth):
            if x[i] != " ":
                break
        c = lenth - 1
        while " " == x[c] and c >= i:
            c -= 1
    return x[i:c+1],
m = input()
print(shan(m))