'''
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
示例:
输入: [1,2,3,4]
输出: [24,12,8,6]
'''

nums = [1, 2, 3, 4]
ls = []
for i in range(len(nums)):
    x = 1
    for j in range(i):
        x = x * nums[j]
    for z in range(i + 1, len(nums)):
        x = x * nums[z]
    ls.append(x)
print(ls)
