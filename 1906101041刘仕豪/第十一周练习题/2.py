'''
2.	请使用“插入排序”的方法对列表里面的元素由大到小进行排序，ls=[10,9,13,5,25,70,2]
'''

def insert(l):
    for i in range(1,len(l)):
        for j in range(i, 0, -1):
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]

    return l
print(insert([10,9,13,5,25,70,2]))