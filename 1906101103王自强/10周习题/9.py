'''给定一个包含 n 个整数的数组 nums，
判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。'''
def fun(nums):
    for a in nums:
        for b in nums:
            for c in nums:
                if a+b+c==0 and a!=b and a!=c and b!=c:
                    print(a,b,c)