'''统计全为 1 的正方形子矩阵
给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。
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
示例 2：
输入：matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
输出：7
解释：
边长为 1 的正方形有 6 个。
边长为 2 的正方形有 1 个。
正方形的总数 = 6 + 1 = 7
'''
import unittest
def fun(matrix):
    n=len(matrix)#高
    m=len(matrix[0])#宽
    tem=0
    for i in range(0,m):
        tem+=matrix[0][i]
    for i in range(1,n):
        tem+=matrix[i][0]
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][j]:
                matrix[i][j]=min(matrix[i-1][j-1],matrix[i][j-1],matrix[i-1][j])+1
                tem+=matrix[i][j]
    return tem
class funTest(unittest.TestCase):
    def test_01(self):
        self.assertEqual(fun(matrix =[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]), 15)
    def test_02(self):
        self.assertEqual(fun(matrix =[

  [1,0,1],
  [1,1,0],
  [1,1,0]
]), 7)
    def test_03(self):
        self.assertEqual(fun(matrix =[
  [1,0,1,1],
  [1,1,0,1],
  [1,1,0,1],
  [1,1,1,1]
]),15)
if __name__ == '__main__':
    unittest.main()