'''
3.	使用“冒泡排序”的方法对列表里面的元素由大到小进行排序，ls=[10,9,13,5,25,70,2]
'''
def maopao(l):
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l
print(maopao([10,9,13,5,25,70,2]))