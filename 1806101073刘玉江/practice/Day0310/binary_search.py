def binary_search(arr,key):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < key:
            start = mid + 1
        elif arr[mid] > key:
            end = mid - 1
        else:
            return mid
    else:
        return -1

arr = [0,1,2,3,6,7,8,10]
print(binary_search(arr,1))