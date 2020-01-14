'''
给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。

 

示例 1：

输入：matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
输出：15
解释：
边长为 1 的正方形有 10 个。
边长为 2 的正方形有 4 个。
边长为 3 的正方形有 1 个。
正方形的总数 = 10 + 4 + 1 = 15.



'''


def countSquares(matrix):
    m, n = len(matrix), len(matrix[0])
    f = [[0] * n for _ in range(m)]
    ans = 0
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                f[i][j] = matrix[i][j]
            elif matrix[i][j] == 0:
                f[i][j] = 0
            else:
                f[i][j] = min(f[i][j - 1], f[i - 1][j], f[i - 1][j - 1]) + 1
            ans += f[i][j]
    return ans