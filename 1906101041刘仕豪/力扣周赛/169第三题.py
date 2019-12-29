def canReach(arr,start):
    men = set()
    t = 0
    while start:
        if start not in men and start+arr[start]<len(arr):
            men.add(start)
            start+=arr[start]
            if arr[start]==0:
                return True
        if start not in men and start - arr[start]>=0:
            men.add(start)
            start-=arr[start]
            if arr[start]==0:
                return True
    return False
print(canReach([3,0,2,1,2], 2))