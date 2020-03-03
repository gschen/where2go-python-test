def smallerNumbersThanCurrent(nums):
    numsx = []
    a = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]>nums[j]:
                a = a + 1
        numsx.append(a)
        a=0
    return numsx
print(smallerNumbersThanCurrent([8,1,2,2,3]))