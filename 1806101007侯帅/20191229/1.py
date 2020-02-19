import random
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        S=[]
        if n%2!=0:
            for i in range(int(n/2)+1):
                S.append(i)
            for j in range(1,int(n/2)+1):
                S.append(-j)
        else:
            for i in range(1,int(n/2)+1):
                S.append(i)
            for j in range(1,int(n/2)+1):
                S.append(-j)
        return S
s=Solution()
print(s.sumZero(5))
