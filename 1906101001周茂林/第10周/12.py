'''
福尔摩斯到某古堡探险，看到门上写着一个奇怪的算式：
ABCDE * ? = EDCBA
他对华生说：“ABCDE应该代表不同的数字，问号也代表某个数字！”
华生：“我猜也是！”
于是，两人沉默了好久，还是没有算出合适的结果来。
请你利用计算机的优势，找到破解的答案。
把 ABCDE 所代表的数字写出来。
'''
for i in range(1, 10):
    for m in range(10000, 100000):
        n = int(str(m)[::-1])
        if m*i == n and str(m)[0] != str(m)[1] and str(m)[2] != str(m)[3] \
                and str(m)[4] != str(m)[0] and str(m)[2] != str(m)[4]:
            print(m)
