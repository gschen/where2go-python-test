'''
有n个人围成一圈，顺序排号。
从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
'''
import numpy as np:
def qq(number):
    number = list(range(1,n+1))
    aa = len(number)
    bb = []
    while aa == 2:
        for i in range(2,aa+1,3):
            bb.append(aa[i])
        npbb = np.array(bb)
        npaa = np.array(aa)
        aa = npaa - npbb
    print(aa[2])