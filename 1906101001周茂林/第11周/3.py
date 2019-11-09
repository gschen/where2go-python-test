'''
使用“冒泡排序”的方法对列表里面的元素由大到小进行排序，ls=[10,9,13,5,25,70,2]
'''
def bubblesort(arr):
    for m in range(len(arr)):
        for n in range(len(arr)-m-1):
            if arr[n] > arr[n+1]: arr[n],arr[n+1] = arr[n+1],arr[n]
    for i in arr:
        print(i,end=' ')






arr = [10,9,13,5,25,70,2]
bubblesort(arr)