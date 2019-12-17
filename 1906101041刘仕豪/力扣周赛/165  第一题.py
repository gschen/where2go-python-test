def shei(moves):
    gezi = [[' ', '  ', '   '], ['  ', ' ', ' '], ['   ', '    ', '     ']]
    T = 0
    for i in range(0,len(moves),2):
        T +=1
        gezi[moves[i][0]][moves[i][1]] = 'X'
    for j in range(1,len(moves),2):
        T +=1
        gezi[moves[j][0]][moves[j][1]] = 'O'
    if (gezi[0][0]=='X' and gezi[0][0]==gezi[0][1] and gezi[0][2] and gezi[0][2] and gezi[0][1]==gezi[0][2]) or (gezi[1][0]=='X' and gezi[1][0]==gezi[1][1] and gezi[1][1]==gezi[1][2] and gezi[1][2]==gezi[1][0]) or (gezi[2][0]=='X' and gezi[2][0]==gezi[2][1] and gezi[2][0]==gezi[2][2] and gezi[2][1]==gezi[2][2]) or (gezi[0][0]=='X' and gezi[0][0]==gezi[1][0] and gezi[0][0]==gezi[2][0] and gezi[1][0]==gezi[2][0]) or (gezi[0][1]=='X' and gezi[0][1]==gezi[1][1] and gezi[0][1]==gezi[2][1] and gezi[2][1]==gezi[1][1]) or (gezi[0][2]=='X' and gezi[0][2]==gezi[1][2] and gezi[0][2]==gezi[2][2] and gezi[1][2]==gezi[2][2]) or (gezi[0][0]=='X' and gezi[0][0]==gezi[1][1] and gezi[0][0]==gezi[2][2] and gezi[1][1]==gezi[2][2]) or (gezi[0][2]=='X' and gezi[0][2]==gezi[2][0] and gezi[0][2]==gezi[1][1] and gezi[1][1]==gezi[2][0]):
        return 'A'
    if (gezi[0][0]=='O' and gezi[0][0]==gezi[0][1] and gezi[0][2] and gezi[0][2] and gezi[0][1]==gezi[0][2]) or (gezi[1][0]=='O' and gezi[1][0]==gezi[1][1] and gezi[1][1]==gezi[1][2] and gezi[1][2]==gezi[1][0]) or (gezi[2][0]=='O' and gezi[2][0]==gezi[2][1] and gezi[2][0]==gezi[2][2] and gezi[2][1]==gezi[2][2]) or (gezi[0][0]=='O' and gezi[0][0]==gezi[1][0] and gezi[0][0]==gezi[2][0] and gezi[1][0]==gezi[2][0]) or (gezi[0][1]=='O' and gezi[0][1]==gezi[1][1] and gezi[0][1]==gezi[2][1] and gezi[2][1]==gezi[1][1]) or (gezi[0][2]=='O' and gezi[0][2]==gezi[1][2] and gezi[0][2]==gezi[2][2] and gezi[1][2]==gezi[2][2]) or (gezi[0][0]=='O' and gezi[0][0]==gezi[1][1] and gezi[0][0]==gezi[2][2] and gezi[1][1]==gezi[2][2]) or (gezi[0][2]=='O' and gezi[0][2]==gezi[2][0] and gezi[0][2]==gezi[1][1] and gezi[1][1]==gezi[2][0]):
        return 'B'
    if T < 9:
        return 'Pending'
    else:
        return 'Draw'

print(shei([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))






#[[0,0],[2,0],[1,1],[2,1],[2,2]]





