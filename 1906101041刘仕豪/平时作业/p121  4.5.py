import random
num=random.randint(0,100)
time=0
while 1:
    putnum=eval(input("请输入您的数字："))
    if type(putnum)==type(2):
        time += 1
        if putnum < num:
            print("遗憾！太小了")
        elif putnum > num:
            print("遗憾！太大了")
        elif putnum == num:
            print("预测{}次，你猜中了".format(time))
            break
    else:
        print("输入内容必须为整数！")



