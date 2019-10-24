'''
14、	本题要求对任意给定的正整数N，求方程X2+Y2=N的全部正整数解。给定的N<=10000,如果有解请输出全部解，如果无解请输出No Solution。
'''

import math
N = int(input("请输入N:"))
jieshu = True
for x in range(1,101):
    for y in range(1,101):
        if N == x**2+y**2 and x<=y:
            print("{}  {}".format(x, y))
            jieshu = False
if jieshu ==True:
    print("No Solution")








