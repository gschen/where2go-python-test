"""
3.	使用“冒泡排序”的方法对列表里面的元素由大到小进行排序，ls=[10,9,13,5,25,70,2]
"""
def maopao(ls):
    num = len(ls)
    for i in range(0,num):
        for m in range(i+1,num):
            if ls[i] < ls[m]:
                ls[i],ls[m] = ls[m],ls[i]

    return ls

l = input("请输入一串数字，以空格分隔：")
mmm = list()
for ii in l.split():
    ii = int(ii)
    mmm.append(ii)
print(maopao(mmm))

