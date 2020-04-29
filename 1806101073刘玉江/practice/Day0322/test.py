def createTargetArray(nums,index):
    target = []
    for i in range(len(nums)):
        target.insert(index[i], nums[i])
    return target


nums = [4,2,1,1]
index = [0,0,2,0]
print(createTargetArray(nums,index))

ls=[1,2,3,4]
ls.insert(5,0)
print(ls)