"""
12、福尔摩斯到某古堡探险，看到门上写着一个奇怪的算式：
ABCDE * ? = EDCBA
他对华生说：“ABCDE应该代表不同的数字，问号也代表某个数字！”
华生：“我猜也是！”
于是，两人沉默了好久，还是没有算出合适的结果来。
请你利用计算机的优势，找到破解的答案。
把 ABCDE 所代表的数字写出来。
答案：21978
"""


a=""

for mm in range(0,100):
    for i in range(10000,100000):
        c = list(str(i))
        c.reverse()
        if c[1]!="0" and c[2]!="0" and c[0]!="0" and c[3]!="0" and c[1]!=c[2]!=c[3]!=c[0]!=c[4]:
            bb = a.join(c)
            # print(int(a.join(c)))
            # print(bb)
            # print(type(c))
            if i * mm == int(bb):

                print(i)
                break