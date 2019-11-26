#求点的运动最短路径
class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        list = []
        a = len(points)
        for i in range(a-1):
            x = abs(points[i][0]-points[i+1][0])
            y = abs(points[i][1]-points[i+1][1])
            if x>=y:
                list.append(x)
            else:
                list.append(y)
        s = 0
        for n in list:
            s = s+n
        return s
