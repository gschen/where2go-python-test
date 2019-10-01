import random
shuiji = random.randint(0,9)
caideshu = input( '请您猜一个0到9的整数：' )
a = int(caideshu)
while a != shuiji:
    for N in range(1,99):
        if a == shuiji:
            print('经过'+str(N)+'次的猜测,',end = '')
        else:
            if a > shuiji:
                print( '真可惜,比答案大了一点.' )
            else:
                print( '真可惜,比答案小了一点.' )
        if a == shuiji:
            break
        a = int(input( '猜错了哦，请再猜一次：' ))
print( '恭喜您猜对了,游戏结束！' )