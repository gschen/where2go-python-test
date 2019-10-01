import random                                  #猜数字
a = random.randint(0,10)
print(a)
N = 0


while True:
    N += 1
    b = int(input("请猜一个数字："))
    if a < b:
        print("遗憾，太大了")
    if a > b:
        print("遗憾，太小了")
    if a == b:
        print("你猜对了，猜了%d次"% N)
        break
