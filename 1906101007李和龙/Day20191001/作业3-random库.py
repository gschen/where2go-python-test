from random import randint                     #100内随机生成5位整数
for a in range(5):
    print(randint(0,101))


for b in range(0,101):                         #100内奇数
    if (b-1)%2 == 0:
        print("%d "%b ,end = "")
print()


import random                                  #随机生成四个字符
c="abcdefghij"
for d in range(4):
    print(random.choice(c))

import random                                  #随机选择一个
e = ["apple","pear","orange","peach"]
print(random.choice(e))

