'''2.	请使用“插入排序”的方法对列表里面的元素由大到小进行排序，ls=[10,9,13,5,25,70,2]'''
def charupaixu(ls):
    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1
        while j >= 0 and key < ls[j]:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key
    return ls