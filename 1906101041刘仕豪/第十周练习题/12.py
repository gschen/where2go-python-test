'''
12、福尔摩斯到某古堡探险，看到门上写着一个奇怪的算式：
ABCDE * ? = EDCBA
他对华生说：“ABCDE应该代表不同的数字，问号也代表某个数字！”
华生：“我猜也是！”
于是，两人沉默了好久，还是没有算出合适的结果来。
请你利用计算机的优势，找到破解的答案。
把 ABCDE 所代表的数字写出来。
'''

for a in range(1,10):
    for b in range(0,10):
        for c in range(0, 10):
            for d in range(0, 10):
                for e in range(1,10):
                    if a != b and a != c and a != d and a != e and b != c and b != d and b != e and c != d and c != e and d != e:
                        if (e*10000+d*1000+c*100+b*10+a)%(a*10000+b*1000+c*100+d*10+e)==0:
                            print(a*10000+b*1000+c*100+d*10+e)