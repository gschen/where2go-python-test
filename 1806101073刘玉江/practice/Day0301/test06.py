arr=[-2,1,-3,4,-1,2,-3,-5,4]
def maxSubArray(arr):
    for i in range(1,len(arr)):
        if arr[i-1]>0:
            arr[i] = arr[i]+arr[i-1]
        # arr[i] = arr[i] + max(arr[i-1],0)
    return max(arr)
print(maxSubArray(arr))