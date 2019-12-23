def findNumbers(nums):
    t = 0
    for i in nums:
        if len(str(i))%2 == 0:
            t+=1
    return t