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
'''
def isPossibleDivide(nums, k):
    if len(nums) % k == 0:
        nums = sorted(nums)
        for i in nums:
            m = min(nums)
            for j in range(k):
                if m in nums:
                    nums.remove(m)
                    m += 1
                else:
                    return False
        return True
    else:
        return False


print(isPossibleDivide([1, 2, 3, 3, 4, 4, 5, 6], 4))
print(isPossibleDivide([15, 16, 17, 18, 19, 16, 17, 18, 19, 20, 6, 7, 8, 9, 10, 3, 4, 5, 6, 20], 5))
