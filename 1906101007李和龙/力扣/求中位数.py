"""给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
"""
def mid_num(nums1,nums2):
    nums = nums1 + nums2
    new_nums = sorted(nums)
    lenth = len(new_nums)
    if lenth % 2 ==0 :
        the_mid_num = (new_nums[int(lenth/2)-1] + new_nums[int(lenth/2)]) / 2
    else:
        the_mid_num = new_nums[int((lenth+1)/2)-1]
    return float(the_mid_num)
if __name__ == "__main__":
    nums1 = list(map(int,input().split(",")))
    nums2 = list(map(int,input().split(",")))
    print(mid_num(nums1,nums2))