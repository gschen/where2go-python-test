'''
给你一个大小为 m x n 的矩阵 mat 和一个整数阈值 threshold。
请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 0 。
示例 1：
输入：mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
输出：2
解释：总和小于 4 的正方形的最大边长为 2
示例 2：
输入：mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
输出：0
'''
import numpy as np
def maxSideLength(mat1, threshold):
    m, n, d = len(mat1), len(mat1[0]), 0
    mat1 = np.mat(mat1)
    for p in range(max(m, n)):
        v = 0
        for i in range(p+1, m):
            for j in range(p+1, n):
                mat2 = mat1[p:i, p:j]
                print(mat2)
                for q in mat2:
                    v += q
                if v <= threshold:
                    d = max(v, d)
    print(d)


maxSideLength([[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]], 4)
maxSideLength([[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]], 1)
