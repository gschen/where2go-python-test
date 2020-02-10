'''
凑算式
A + B/DEF + C/GHI = 10
这个算式中A-I代表1-9的数字，不同的字母代表不同的数字。
比如：
6+8/3+952/714 就是一种解法，
5+3/1+972/486 是另一种解法。
这个算式一共有多少种解法？
'''
s = 0
for A in range(1, 10):
    for B in range(1, 10):
        for C in range(1, 10):
            for D in range(1, 10):
                for E in range(1, 10):
                    for F in range(1, 10):
                        for G in range(1, 10):
                            for H in range(1, 10):
                                for I in range(1, 10):
                                    if len(set(list('ABCDEFGHI'))) == 9 and A + B/D*100+E*10+F + C/G*100+H*10+I == 10:
                                        s += 1
print(s)

