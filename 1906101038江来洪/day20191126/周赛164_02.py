"""这里有一幅服务器分布图，服务器的位置标识在m*n的整数矩阵网格grid中，1 表示单元格上有服务器，0 表示没有。
如果两台服务器位于同一行或者同一列，我们就认为它们之间可以进行通信。
请你统计并返回能够与至少一台其他服务器进行通信的服务器的数量。
"""
def jiang(grid):
    def jiang1(y):
        list = []
        for l in grid:
            list.append(l[y])
        return list
    num = 0
    for o in grid:
        for p in o:
            if p == 1:
                num += 1
    a = len(grid)
    b = len(grid[0])
    c = a * b
    x, y, s = 0, 0, 0
    for i in range(c):
        if grid[x][y] == 1:
            if sum(grid[x]) == 1 and sum(jiang1(y)) == 1:
                s += 1
        if y == b - 1:
            x += 1
            y = 0
        else:
            y += 1
    return num - s
print(jiang([[0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 1], [1, 0, 0, 1]]))


