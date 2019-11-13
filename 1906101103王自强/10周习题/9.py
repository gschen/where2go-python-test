'''给定一个包含 n 个整数的数组 nums，
判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。'''
def fun(nums):
    box=[]
    for a in range(len(nums)):
        for b in range(len(nums)):
            for c in range(len(nums)):
                if nums[a]+nums[b]+nums[c]==0 and a<b<c:
                    x=[nums[a],nums[b],nums[c]]
                    box.append(x)
    print(box)
nums=[-1,0,1,2,-1,-4]
fun(nums)