def countServers(grid):
    n = 0
    le = len(grid[0])
    for i in grid:
        m = 0
        for j in i:
            if j == 1:
                m += 1
        if m > 1:
            n += m
    for p in range(len(grid)):
        for g in range(len(grid)):
            for f in range(le):
                if p != g and grid[p][f] == grid[g][f] == 1 and 1 not in grid[g][:f] and 1 not in grid[g][f+1:]:
                    n += 1
    print(n)

countServers([[1,1,0,1,0],[0,0,0,0,0],[0,0,0,1,0]])

