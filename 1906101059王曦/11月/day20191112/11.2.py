#用“插入排序”的方法对列表里面的元素由大到小进行排序，ls=[10,9,13,5,25,70,2]
def wxsort(ls):
    for n in range(1,len(ls)):
        s = ls[n]
        for i in range(n-1,-1,-1):
            if ls[i] > s:
                ls[i+1] = ls[i]
                ls[i] = s
    return ls

ls = [10,9,13,5,25,70,2]
print(wxsort(ls))