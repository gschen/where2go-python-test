'''
给你一个整数数组 nums 和一个正整数 k，请你判断是否可以把这个数组划分成一些由 k 个连续数字组成的集合。
如果可以，请返回 True；否则，返回 False。



示例 1：

输入：nums = [1,2,3,3,4,4,5,6], k = 4
输出：true
解释：数组可以分成 [1,2,3,4] 和 [3,4,5,6]。
示例 2：

输入：nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
输出：true
解释：数组可以分成 [1,2,3] , [2,3,4] , [3,4,5] 和 [9,10,11]。
示例 3：

输入：nums = [3,3,2,2,1,1], k = 3
输出：true
示例 4：

输入：nums = [1,2,3,4], k = 3
输出：false
解释：数组不能分成几个大小为 3 的子数组
'''


def isPossibleDivide(nums, k):
    nums = sorted(nums)
    for _ in range(len(nums)//k):
        a = nums[0]
        for _ in range(k):
            if a in nums:
                nums.remove(a)
                a+=1
    return len(nums) == 0
print(isPossibleDivide([3,2,1,5,6,8],3))
