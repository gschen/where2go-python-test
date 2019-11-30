class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        mindistance = 0
        for i in range(len(points)-1):
            if points[i+1][1]>points[i][1]:
                maxmun=points[i+1][1]
                minmun=points[i][1]
            elif points[i+1][1]<points[i][1]:
                maxmun=points[i][1]
                minmun=points[i+1][1]
            if  points[i][1]!=points[i+1][1]:
                a = 1
            elif points[i][1]==points[i+1][1]:
                a = 0
            mindistance = mindistance + abs(points[i+1][0]-points[i][0])+a*abs(maxmun-abs(points[i+1][0]-points[i][0])-minmun)
        return mindistance
if __name__ =='__main__':
    solution = Solution()
    point= [[1,1],[3,4],[-1,0]]
    print(solution.minTimeToVisitAllPoints(point))