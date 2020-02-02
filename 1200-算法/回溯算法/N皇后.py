N = 4

board = [['.' for i in range(N)] for j in range(N)]

result = []

def is_valid(board, row, col):
    n = len(board)

    # 检查列
    for i in range(n):
        if board[i][col] == 'Q':
            return False
    
    # 检查左上方
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1
    
    # 检查右上方
    i = row - 1
    j = col + 1
    while j < n and i >= 0:
        if board[i][j] == 'Q':
            return False
        
        i = i - 1
        j = j + 1

    return True

def backtrack(board, row):
    n = len(board)

    if row == n:
        print(board)
        result.append(list(board))
        return 
    
    for col in range(n):

        if is_valid(board, row, col) == False:
            continue

        board[row][col] = 'Q'
        backtrack(board, row + 1)
        board[row][col] = '.'

backtrack(board, 0)

print(result)
