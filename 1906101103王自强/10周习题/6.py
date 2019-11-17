'''6、	给定一个整数数组 nums 和一个目标值 target，
请你在该数组中找出和为目标值的那 两个 整数
，并返回他们的数组下标。
 '''
def fun(nums,target):
    if len(nums)<2:
        return
    for i in range(0,len(nums)):
        for j in range(0,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]