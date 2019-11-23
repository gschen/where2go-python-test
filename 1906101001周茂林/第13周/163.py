class Solution:
    def shiftGrid(grid, k):
        lis = []
        x = len(grid[0])
        y = len(grid)
        for i in grid:
            for j in i:
                lis.append(j)
        lis2,lis3 = lis[:-k],lis[-k:][::-1]
        lis = lis3 + lis2
        lis4 = []
        for i in range(y):
            lis4.append([lis[i*x],lis[i*x+1],lis[i*x+2]])
        print(lis4)


    shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1)
