x = 2
n = 1
i = 0
import random
true_num = (random.choice(range(10)))
while i <= x:
    guess_num = int(input('请输入一个数字：'))
    while guess_num != true_num:
        n += 1
        if guess_num < true_num:
            print('太小了！')
            guess_num = int(input('请再猜一个数字：'))
        elif guess_num > true_num:
            print('太大了！')
            guess_num = int(input('请再一个数字：'))
    print('恭喜你，猜了%d次，猜中了' % n)
    i += 1
    print('你已经玩了%d局猜数字游戏了，你还想玩吗?'% i)
    m = int(input('0(不完了) or 1(再来一次)? :'))
    n = 1
    if m == 1:
        true_num = (random.choice(range(10)))
    else:
        print('感谢参与！')
        break
print('对不起，你今日游戏次数已上限，请明天再来！')

