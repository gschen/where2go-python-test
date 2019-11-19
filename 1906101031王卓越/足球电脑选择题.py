from random import choice
dict = ['left','center','right']
b = 0
c = 0
i = 1
while i < 6:
    print("你所选择的方向: 'left','center','right'")
    x=input()
    i=i+1
    a = choice(dict)    
    if x != a:
        b = b + 1
        print("你的当前分数")
        print(b)
    else:
        c = c + 1
        print("电脑的当前分数")
        print(c)
print("你的总分得分:%d" % b)
print("电脑的总得分:%s" % c)



