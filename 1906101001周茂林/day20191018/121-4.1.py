import random
a = random.randint(0,9)
b = int(input( '请您猜一个0到9的整数：' ))
n = 1
while b != a:
    n += 1
    if b > a:
        print( '真可惜,比答案大了一点.' )
    else:
        print( '真可惜,比答案小了一点.' )
    b = int(input( '请再猜一次：' ))
print('经过'+str(n)+'次的猜测,恭喜您猜对了')