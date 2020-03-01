#     小明先把硬币摆成了一个 n 行 m 列的矩阵。
#
#     随后，小明对每一个硬币分别进行一次 Q 操作。
#
#     对第x行第y列的硬币进行 Q 操作的定义：将所有第 i*x 行，第 j*y 列的硬币进行翻转。
#
#     其中i和j为任意使操作可行的正整数，行号和列号都是从1开始。
#
#     当小明对所有硬币都进行了一次 Q 操作后，他发现了一个奇迹——所有硬币均为正面朝上。
#
#     小明想知道最开始有多少枚硬币是反面朝上的。于是，他向他的好朋友小M寻求帮助。
#
#     聪明的小M告诉小明，只需要对所有硬币再进行一次Q操作，即可恢复到最开始的状态。然而小明很懒，不愿意照做。于是小明希望你给出他更好的方法。帮他计算出答案。
#
# 【数据格式】
#     输入数据包含一行，两个正整数 n m，含义见题目描述。
#     输出一个正整数，表示最开始有多少枚硬币是反面朝上的。


#思路：找到哪些（x，y）是翻动之后变化的，当（x，y）翻动的次数=x行翻动的次数*y列翻动的次数为奇数，才会发生变化
#举例：（2，4）这个点被翻动的次数是（1，1），（1，2），（1，4），（2，2），（2，4），（4，4）这些点在进行q操作时翻动的。
#此时，先考虑列，第y列被翻动的次数=y的因子的个数
#再考虑行，第x行被翻动的次数=x的因子的个数
#我们知道，只有当奇数*奇数才会是奇数，所以，只需要知道n行m列中哪些行和列的因子同时为奇数即可
#且只有平方数的因子个数为奇数（质数和偶数的因子成对出现）
#n下包含的平方数的个数为sqrt（n）向下取整。
#所以问题转变成了求sqrt（n）*sqrt（m）
#所以问题也就迎刃而解了
import time
import math
import numpy as np

n,m=input().split(' ')
def fanyingbi(n,m):
    if len(n) % 2 == 0:
        n_len = len(n) / 2
    else:
        n_len = (len(n) // 2) + 1
    n_len = int(n_len)
    n_1 = []
    n_2 = []
    for i in range(n_len):#构建全为0的列表模拟平方根
        n_1.append('0')
    for i in range(n_len):
        n_2.append('0')
    for x in range(n_len):
        for y in range(1, 10):
            n_1[x] = str(y)#将（1-9）插入x位置
            n_2[x] = str(y - 1)#同时不要忘记0的情况
            a = ''.join(n_1)#字符串化
            b = ''.join(n_2)
            if eval(a) ** 2 > eval(n) and eval(b) ** 2 <= eval(n):#当平方根满足条件时，跳出循环
                break
    n_sum = eval(''.join(n_2))


    if len(m) % 2 == 0:
        m_len = len(m) / 2
    else:
        m_len = (len(m) // 2) + 1
    m_len = int(m_len)
    m_1 = []
    m_2 = []
    for i in range(n_len):#构建全为0的列表模拟平方根
        m_1.append('0')
    for i in range(n_len):
        m_2.append('0')
    for x in range(m_len):
        for y in range(1, 10):
            m_1[x] = str(y)#将（1-9）插入x位置
            m_2[x] = str(y - 1)#同时不要忘记0的情况
            a = ''.join(m_1)#字符串化
            b = ''.join(m_2)
            if eval(a) ** 2 > eval(n) and eval(b) ** 2 <= eval(n):#当平方根满足条件时，跳出循环
                break
    m_sum=eval(''.join(m_2))
    return  n_sum*m_sum















