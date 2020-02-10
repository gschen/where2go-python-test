def isPossibleDivide(nums, k):
    if len(nums) % k != 0:
        return False
    for _ in range(len(nums) // k):
        for i in range(min(nums),min(nums)+k+1):
            if i in  nums:
                nums.remove(i)
    if len(nums) == 0:
        return True
    else:
        return False
print(isPossibleDivide([3,2,1,5,6,8],3))