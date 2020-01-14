class Solution:
    def sumZero(self, n: int) -> List[int]:
        import numpy as np
        List=[]
        if n%2==0:
            for i in range(1,(n+2)//2):
                List.append(i)
                List.append(-i)
        if n%2!=0:
            List.append(0)
            for i in range(1,(n+1)//2):
                List.append(i)
                List.append(-i)
        return sorted(np.array(List))



