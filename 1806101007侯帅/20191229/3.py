from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def hanshu(start):
            while arr[start+arr[start]]!=0 or arr[start-arr[start]]!=0:
                start=start+arr[start]
                hanshu(start)
            else:
                return True
        hanshu(start)
        return True


