'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

'''


def searchRange(self, nums, target):
    # find the index of the leftmost appearance of `target`. if it does not
    # appear, return [-1, -1] early.
    for i in range(len(nums)):
        if nums[i] == target:
            left_idx = i
            break
    else:
        return [-1, -1]
    for j in range(len(nums) - 1, -1, -1):
        if nums[j] == target:
            right_idx = j
            break

    return [left_idx, right_idx]


