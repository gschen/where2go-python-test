"""
6、	给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
"""
nums = [2,7,11,15]
target = 9
c= list()
for m in nums:
    for n in nums:
        if m + n == target and m < n:
            print(m,n)
            a = nums.index(m)
            b = nums.index(n)
            c.append(a)
            c.append(b)
            print(c)