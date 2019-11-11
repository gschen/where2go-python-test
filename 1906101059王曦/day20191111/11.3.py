#3.	使用“冒泡排序”的方法对列表里面的元素由大到小进行排序，ls=[10,9,13,5,25,70,2]
def wxsort(ls):
    for n in range(len(ls)-1):
        for i in range(len(ls)-n-1):
            if ls[i]>ls[i+1]:
                ls[i],ls[i+1]=ls[i+1],ls[i]
    return ls


ls = [10,9,13,5,25,70,2]
print(wxsort(ls))