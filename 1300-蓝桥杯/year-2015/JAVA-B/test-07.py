'''牌型种数
小明被劫持到X赌城，被迫与其他3人玩牌。
一副扑克牌（去掉大小王牌，共52张），均匀发给4个人，每个人13张。
这时，小明脑子里突然冒出一个问题：
如果不考虑花色，只考虑点数，也不考虑自己得到的牌的先后顺序，自己手里能拿到的初始牌型组合一共有多少种呢？
'''
sum=0
for a1 in range(0,5):
    for a2 in range(0, 5):
        for a3 in range(0, 5):
            for a4 in range(0, 5):
                for a5 in range(0, 5):
                    for a6 in range(0, 5):
                        for a7 in range(0, 5):
                            for a8 in range(0, 5):
                                for a9 in range(0, 5):
                                    for a10 in range(0, 5):
                                        for aj in range(0, 5):
                                            for aq in range(0, 5):
                                                for ak in range(0, 5):
                                                     if a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+aj+aq+ak==13:
                                                         sum+=1
print(sum)