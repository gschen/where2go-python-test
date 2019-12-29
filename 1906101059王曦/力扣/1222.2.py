# 给你一个整数数组 nums 和一个正整数 k，请你判断是否可以把这个数组划分成一些由 k 个连续数字组成的集合。
# 如果可以，请返回 True；否则，返回 False。
nums = [1,2,3,3,4,4,5,6]
k = 4
if len(nums)%k==0:
    while len(nums)!=0:
        d = k
        a = min(nums)
        while d>0:
            if a in nums:
                nums.remove(a)
                a+=1
                d-=1
        if a not in nums:
            break
    if len(nums)==0:
        print('ture')
    else:
        print('false')
else:
    print('false')