from typing import List
import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        li = []
        for i in range(1,max(nums) + 1, 1):
            a = 0
            for j in nums:
                a+= math.ceil(j/i)
            if a <= threshold:
                li.append(i)
        return (min(li))
if __name__=='__main__':
    solution=Solution()
    s = [19]
    k = 5
    print(solution.smallestDivisor(s,k))








