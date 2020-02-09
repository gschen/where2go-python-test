class Solution:
    def maxSideLength(self, mat, threshold):
        import numpy as np
        mat=np.array(mat)
        lis1=[]
        lis2=[]
        w=len(mat)
        h=len(mat[0])
        lis2.append(w)
        lis2.append(h)
        s=min(lis2)
        print(s)
        for x in range(s):
            for y in range(s):
                map = [[1 for j in range(1,x+2)] for j in range(1,x+2)]
                print(map)
                mat[x][y]=np.sum(mat[x:x+x,y:y+y]*map)
                if mat[x][y]<=threshold:
                    lis1.append(x)
        return max(lis1)

if __name__ =='__main__':
    solution = Solution()
    point=[[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]]
    th=40184
    print(solution.maxSideLength(point,th))








