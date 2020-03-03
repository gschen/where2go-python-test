def findSpecialInteger(arr):
    len_arr = len(arr)
    dic = {}
    for i in range(len_arr):
        if arr[i] in dic:
            dic[arr[i]] += 1
        else:
            dic[arr[i]] = 1
    for i in dic:
        if dic[i]/len_arr>0.25:
            return i
print(findSpecialInteger([1,1,3,5,9,9,2,2,6,6,6,6,7,10]))
