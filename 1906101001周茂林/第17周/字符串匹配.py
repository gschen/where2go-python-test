def sunday(S, T):
    ls, lt = len(S), len(T)
    d = 0
    #记录下标
    while d <= ls - lt and T in S:
        #保证T有成为S子串的前提下并且循环
        if S[d:d+lt] == T:
            #如果符合，返回下标
            return d
        else:
            p = T.rfind(S[d+lt])
            #返回字符串最后一次出现的位置，如果没有匹配项则返回-1
            if p == -1:
                #没有匹配，跳子串长度个距离
                d += lt + 1
            else:
                #有匹配，对齐查看是否全部匹配
                d += lt - p
    return False


print(sunday('abcabeabd', 'abd'))
