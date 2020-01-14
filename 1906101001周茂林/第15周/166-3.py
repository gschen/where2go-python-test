'''
给你一个整数数组 nums 和一个正整数 threshold  ，你需要选择一个正整数作为除数，然后将数组里每个数都除以它，并对除法结果求和。
请你找出能够使上述结果小于等于阈值 threshold 的除数中 最小 的那个。
每个数除以除数后都向上取整，比方说 7/3 = 3 ， 10/2 = 5 。
示例 1：
输入：nums = [1,2,5,9], threshold = 6
输出：5
解释：如果除数为 1 ，我们可以得到和为 17 （1+2+5+9）。
如果除数为 4 ，我们可以得到和为 7 (1+1+2+3) 。如果除数为 5 ，和为 5 (1+1+1+2)。
'''
def smallestDivisor(nums, threshold):
    import math
    for i in range(1, max(nums)):
        m = 0
        for j in nums:
            m += math.ceil(j / i)
        if m <= threshold:
            return i


print(smallestDivisor([1, 2, 5, 9], 6))
print(smallestDivisor([2, 3, 5, 7, 11], 11))
print(smallestDivisor([19], 5))
