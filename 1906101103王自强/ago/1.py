import random
i=0
a=random.randint(0,101)
while True:

    try:
        b=eval(input("请输入一个0~100的整数:"))
        print(num**2)
    except NameError:
        print('输入错误，请输入一个0~100的整数')
        b=int(b)
    if b>a:
        print("遗憾太大了")
    elif b==a:
        print("预测%d次，你猜中了"%i)
    else:
        print("遗憾太小了")