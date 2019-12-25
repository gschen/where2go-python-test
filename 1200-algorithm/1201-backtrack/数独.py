'''

编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。

'''

result = []

# N = 9

# board = [['.' for j in range(N)] for i in range(N)]

def is_valid(board, row, col, num):

    n = len(board)

    # 每一列不能重复
    for i in range(n):
        if board[i][col] == num:
            return False

    # 每一行不能重复
    for i in range(n):
        if board[row][col] == num:
            return False

    # 每一宫不能重复
    r = row // 3
    c = col // 3
    for i in range(r*3, r*3 + 3):
        for j in range(c*3, c*3 +3):
            if board[i][j] == num:
                return False

    return True


def is_finished(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                return False

    return True

def backtrack(board, row, col):
    print(row, col)

    if row == 9 and col == 9:
        print(board)
        return 

    for num in range(1, 10):
        if is_valid(board, row, col, num) == False:
            continue
        
        board[row][col] = str(num)

        if col == 8:
            backtrack(board, row+1, 0)
        else:
            backtrack(board, row, col+1)
        
        board[row][col] = '.'



board = [
    ['5','3','.','.','7','.','.','.','.'],
    ['6','.','.','1','9','5','.','.','.'],
    ['.','9','8','.','.','.','.','6','.'],
    ['8','.','.','.','6','.','.','.','3'],
    ['4','.','.','8','.','3','.','.','1'],
    ['7','.','.','.','2','.','.','.','6'],
    ['.','6','.','.','.','.','2','8','.'],
    ['.','.','.','4','1','9','.','.','5'],
    ['.','.','.','.','8','.','.','7','9'],
]

for i in range(9):
    for j in range(9):
        if board[i][j] == '.':
            backtrack(board, i, j)