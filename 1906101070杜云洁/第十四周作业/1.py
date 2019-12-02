nums=[1,1,1,2,3,4,4,4,4]
for i in range(len(nums)-1):
    for a in nums[i+1: ]:
        if nums[i]==a:
            nums.remove(nums[i])
        else:
            break
print(len(nums))
print(nums)