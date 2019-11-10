'''
请使用“插入排序”的方法对列表里面的元素由大到小进行排序，ls=[10,9,13,5,25,70,2]
'''
def crpx(ls):
    for i in range(1,len(ls)):
        k = ls[i]
        q = i - 1
        while q >= 0 and k < ls[q]:
            ls[q+1] = ls[q]
            q -= 1
        ls[q+1] = k
    for o in range(len(ls)):
        print(ls[o],end=' ')



ls = [10,9,13,5,25,70,2]
crpx(ls)