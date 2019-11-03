'''
给定一个包含 n 个整数的数组 nums.
判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
'''
def numsabc(nums):
    for a in nums:
        nums.pop(a)
        for b in nums:
            nums.pop(b)
            for c in nums:
                if a <= b <= c and a+b+c == 0:
                    print(a,b,c)



numsabc([-1,0,1,2,-1,-4])