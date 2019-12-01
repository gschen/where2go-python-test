class Solution:
    def minTimeToVisitAllPoints(points):
        lis1 = []
        lis2 = []
        for i in points:
            lis1.append(i[0])
            lis2.append(i[1])
        m,n = 0,0
        for j in range(len(lis1)-1):
            m += abs(lis1[j]-lis1[j+1])
        for k in range(len(lis2)-1):
            n += abs(lis2[k]-lis2[k+1])
        if m >= n:
            print(m)
        else:
            print(n)
    minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])
