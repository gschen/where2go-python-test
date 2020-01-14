class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        import numpy as np
        nums = np.array(nums)
        b=0
        for i in nums:
            a=len(str(i))
            if a%2==0:
                b+=1
        return b



