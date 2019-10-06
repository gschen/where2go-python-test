try:
    s = eval(input("请输入一个整数："))
except NameError:
    print("输入错误，请输入一个整数")
else:
    if s > 5:
        print("遗憾，太大了")
    if s < 5:
        print("遗憾，太小了")
    if s == 5:
        print("你猜中了")