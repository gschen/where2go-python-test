import numpy as np
def tong(grid):
    t = 0
    a = np.shape(grid)
    grid = np.array(grid)
    grid = np.ravel(grid)
    m = a[1]
    grid = list(grid)

    while m > 0:
        grid.insert(0,0)
        grid.append(0)
        m -= 1
    for i in range(a[1],len(grid)-a[1]):
        if grid[i] == 1 and (grid[i] == grid[i-1]  or grid[i] == grid[i+1] or grid[i] == grid[i+a[1]] or grid[i] == grid[i-a[1]]):
            t += 1
    return t
print(tong([[1,0,0,1,0],[0,0,0,0,0],[0,0,0,1,0]]))

