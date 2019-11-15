'''
取球博弈。
今盒子里有n个小球, A、B两人轮流从盒中取球，每个人都可以看到另一个人取了多少个，.
也可以看到盒中还剩下多少个，并且两人都很聪明，不会做出错误的判断。
我们约定:
每个人从盒子中取出的球的数目必须是: 1, 3, 7, 8。
轮到某一方取球时不能弃权!。
A先取球，然后双方交替取球，直到取完。
被迫拿到最后-一个球的一方为负方(输方)。
请编程确定出在双方都不判断失误的情况下，对于特定的初始球数，A是否能贏?。
程序运行时，从标准输入获得数据，其格式如下:。
先是一个整数n(n<100),表示接下来有n个整数。然后是n个整数,每个占--行(整数<10000),
表示初始球数。。
程序则输出n行，表示A的输赢情况(输为0，赢为1)。。
例如，用户输入:。
4
1
2
10
18
则程序应该输出:
0
1
1
0
'''
def bisai(m):
    t = 0
    while m > 15:
        m -= 15
    if m < 8 and m%2 == 1:
        return 0
    else:
        return 1

def quqiu():
    n = int(input())
    l = []
    while n > 0:
        a = int(input())
        l.append(a)
        n -= 1
    for i in l:
        print(bisai(i))

quqiu()


