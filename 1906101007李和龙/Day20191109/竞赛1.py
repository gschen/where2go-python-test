"""
Tairitsu 被鲜花所包围，她似乎已经忘记了，那身边的恶浊的 Arcaea，那曾经的痛苦与忧愁。
鲜花围成了一个圆的形状，Tairitsu 将花圈放在了地上。
花圈的圆心坐标为 (a,b)(a,b)，半径为 rr。
地面上共有 nn 个 Arcaea，我们将每个 Arcaea 看成 11 个点，第 ii 个 Arcaea 的坐标为 (x_i,y_i)(x-i,y_i)。
Tairitsu 想知道，花圈内（含边界）有多少个 Arcaea 呢？
注：就算存在多个 Arcaea 在同一个坐标，个数也要重复计算，详情见样例 2。
"""
n, a, b, r = map(int, input().split())
o = 0
for mm in range(n):
    x, y = map(int, input().split())
    if ((x - a) ** 2 + (y - b) ** 2) <= r ** 2:
        o += 1
print(o)

