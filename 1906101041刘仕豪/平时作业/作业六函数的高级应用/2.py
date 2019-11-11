'''
写一个函数，函数内部使用迭代查找list当中的最大值和最小值，返回一个元组。
'''
def b(l):
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return (l[0],l[-1])
print(b([32,5,12,3]))