#找出井字棋的获胜者
class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        set1 = {0,1,2}
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        for i in range(0,len(moves),2):
            if i<len(moves):
                list3.append(moves[i][0])
                list4.append(moves[i][1])
        for n in range(1, len(moves), 2):
            if n<len(moves):
                list5.append(moves[n][0])
                list6.append(moves[n][1])
        if set(list3)==set1 or set(list4) == set1 and set(list5)!=set1 and set(list6)!= set1:
            return('A')
        if set(list5)==set1 or set(list6)== set1 and set(list3)!=set1 and set(list4) != set1:
            return('B')
        if len(moves)<9 and set(list3)!=set1 and set(list4) != set1 and set(list5)!=set1 and set(list6)!= set1:
            return('Draw')
        if len(moves)==9 and set(list3)!=set1 and set(list4) != set1 and set(list5)!=set1 and set(list6)!= set1 :
            return('Pending')