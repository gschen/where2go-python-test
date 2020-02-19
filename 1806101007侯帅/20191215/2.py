from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        S=[]
        for i in range(low,high):
                for j in range(0,len(str(i))-1):
                    if int(str(i)[j])==int(str(i)[j+1])-1:
                        S.append(i)
        return S
so=Solution()
test1=so.sequentialDigits(10,300)
print(test1)
