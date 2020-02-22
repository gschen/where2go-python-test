from itertools import groupby
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        # S=[]
        # for i in range(0,len(nums)-1):
        #     S.append(nums[i])
        #     for j in nums:
        #         if j==nums[i]:
        #             S.append(j)
        global scop
        fun = lambda x: x[1] - x[0]
        L=[]
        for l, g in groupby(enumerate(nums), fun):
            l1 = [j for i, j in g]  # 连续数字的列表
            L.append(len(l1))







