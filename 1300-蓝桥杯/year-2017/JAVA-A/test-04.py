vis = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0


def dfs(x, y):
    global vis
    global ans
    global dx
    global dy
    if x == 0 or x == 6 or y == 0 or y == 6:
        ans += 1
        return
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if vis[a][b]:
            continue
        vis[a][b] = 1
        vis[6 - a][6 - b] = 1
        dfs(a, b)
        vis[a][b] = 0
        vis[6 - a][6 - b] = 0


vis[3][3] = 1
dfs(3, 3)
print(ans / 4)
