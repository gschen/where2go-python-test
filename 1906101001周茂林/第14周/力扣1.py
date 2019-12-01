'''
A 和 B 在一个 3 x 3 的网格上玩井字棋。
井字棋游戏的规则如下：
玩家轮流将棋子放在空方格 (" ") 上。
第一个玩家 A 总是用 "X" 作为棋子，而第二个玩家 B 总是用 "O" 作为棋子。
"X" 和 "O" 只能放在空方格中，而不能放在已经被占用的方格上。
只要有 3 个相同的（非空）棋子排成一条直线（行、列、对角线）时，游戏结束。
如果所有方块都放满棋子（不为空），游戏也会结束。
游戏结束后，棋子无法再进行任何移动。
给你一个数组 moves，其中每个元素是大小为 2 的另一个数组（元素分别对应网格的行和列）
它按照 A 和 B 的行动顺序（先 A 后 B）记录了两人各自的棋子位置。
如果游戏存在获胜者（A 或 B），就返回该游戏的获胜者；如果游戏以平局结束，则返回 "Draw"；如果仍会有行动（游戏未结束），则返回 "Pending"。
你可以假设 moves 都 有效（遵循井字棋规则），网格最初是空的，A 将先行动。
'''
def ABmove(moves):
    lis1 = [' ' for x in range(9)]
    n = 0
    for i in moves:
        for j in i[0:1]:
            if n % 2 == 0:
                lis1[j * 3 + i[1]] = 1
            else:
                lis1[j * 3 + i[1]] = 0
            n += 1
    for q in range(3):
        if lis1[q*3] == lis1[1+q*3] == 1 and lis1[1+q*3] == lis1[2+q*3] == 1:
            print('A')
            break
        elif lis1[q*3] == lis1[1+q*3] == 0 and lis1[1+q*3] == lis1[2+q*3] == 0:
            print('B')
            break
        elif lis1[q] == lis1[q+3] == 1 and lis1[q+6] == lis1[q+3] == 1:
            print('A')
            break
        elif lis1[q] == lis1[q+3] == 0 and lis1[q+6] == lis1[q+3] == 0:
            print('B')
            break
        elif lis1[0] == lis1[4] == 1 and lis1[4] == lis1[8] == 1:
            print('A')
            break
        elif lis1[2] == lis1[4] == 1 and lis1[4] == lis1[6] == 1:
            print('A')
            break
        elif lis1[0] == lis1[4] == 0 and lis1[4] == lis1[8] == 0:
            print('B')
            break
        elif lis1[2] == lis1[4] == 0 and lis1[4] == lis1[6] == 0:
            print('B')
            break
    else:
        if lis1.count(' ') == 0:
            print('Draw')
        else:
            print('Pending')

ABmove([[0,0],[2,0],[1,1],[2,1],[2,2]])