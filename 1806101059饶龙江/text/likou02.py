import numpy as np
class Solution(object):
    def countServers(self, grid):
        B = np.pad(grid,((1,1),(1,1)),'constant',constant_values=(0,0))
        n =0
        for i in range(1,len(B)-1):
            for j in range(1,len(B[i])-1):
                if B[i][j]==1 :
                    if B[i+1][j]==1 or B[i][j+1]==1 or B[i-1][j]==1 or B[i][j-1]==1:
                        n = n +1
        return n
if __name__ =='__main__':
    solution=Solution()
    grid=[[1,1,1,1],[0,0,0,0],[1,1,0,0],[1,0,0,0]]
    print(solution.countServers(grid))







