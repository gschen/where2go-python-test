def countServers(grid):
    n = 0
    for i in grid:
        if i.count(1) > 1:
            n += i.count(1)
    for j in range(len(grid)):
        for g in range(len(grid)):
            for f in range(len(grid[0])):
                if j != g and grid[j][f] == grid[g][f] == 1 and grid[g].count(1) == 1:
                    n += 1
    print(n)

countServers([[1,1,0,1,0],[0,0,0,0,0],[0,0,0,1,0]])
