#周赛第一题
class Solution:
    def sumZero(self, n: int) -> List[int]:
        l = list(range(n-1))
        l.append(-(sum(l)))
        return l
