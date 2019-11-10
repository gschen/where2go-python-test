'''
给定一个整数数组 nums 和一个目标值 target,请你在该数组中找出和为目标值的那两个整数,并返回他们的数组下标。
'''
def numstarget(nums,target):
    for m in nums:
        for n in nums:
            if m < n and m+n == target:
                print(nums.index(m),nums.index(n))


numstarget([2,7,11,15],9)