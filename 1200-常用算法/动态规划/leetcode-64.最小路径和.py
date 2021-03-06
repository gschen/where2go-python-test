'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def f(grid):
    
    m = len(grid)
    n = len(grid[0])

    if m == 1 and n == 1:
            return grid[0][0]

    a = [[0 for i in range(n+1)] for j in range(m+1)]
    
    a[1][1] = grid[0][0]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            val, up, left = grid[i-1][j-1],0,0

            if i - 1 > 0:
                up = a[i-1][j]
            else:
                a[i][j] = val + a[i][j-1]
                continue

            if j - 1 > 0:
                left = a[i][j-1] 
            else:
                a[i][j] = val + a[i-1][j]
                continue
            
            if up <= left:
                a[i][j] = up + val
            else:
                a[i][j] = left + val

    return a[-1][-1]


a = [[0,2,2,6,4,1,6,2,9,9,5,8,4,4],[0,3,6,4,5,5,9,7,8,3,9,9,5,4],[6,9,0,7,2,2,5,6,3,1,0,4,2,5],[3,8,2,3,2,8,8,7,5,9,6,3,4,5],[4,0,1,3,9,2,0,1,6,7,9,2,8,9],[6,2,7,9,0,9,5,2,7,5,1,4,4,7],[9,8,3,3,0,6,8,0,8,8,3,5,7,3],[7,7,4,5,9,1,5,0,2,2,2,1,7,4],[5,1,3,4,1,6,0,4,3,8,4,3,9,9],[0,6,4,9,4,1,5,5,4,2,5,7,4,0],[0,1,6,6,4,9,2,7,8,2,1,3,3,7],[8,4,9,9,2,3,8,6,6,5,4,1,7,9]]

print(f(a))