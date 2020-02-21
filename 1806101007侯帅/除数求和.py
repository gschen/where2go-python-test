import math
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        #遍历除数
        L={}
        S = []
        for j in range(1,max(nums)+1):
            Sum=0
            for i in nums:
                chushu=math.ceil(i/j)
                Sum+=chushu
            L[j]=Sum
        for k,z in L.items():
            if z<=threshold:
                S.append(k)
        return min(set(S))
a=Solution()
c=a.smallestDivisor([2,3,5,7,11],11)
print(c)
