#统计列表中偶数位数字个数
def jiang(nums):
    num = 0
    for i in nums:
        if len(str(i)) % 2 == 0:
            num += 1
    return num
print(jiang([1,34,56,45,345,2345]))