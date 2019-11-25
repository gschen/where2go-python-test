def quick_sort(b):
    b=arr=[]
    if len(b)<2:
        return arr
    mid=arr[len(b)//2]
    left,right=[],[]
    b.remove(mid)
    for item in range(b):
        if item>=mid:
            right.append(item)
        else:
            left.append(item)
    return quick_sort(left)+[mid]+quick_sort(right)



b=[2,1,3,5,4]
quick_sort(b)


