#假设 a b c d e 代表1~9不同的5个数字（注意是各不相同的数字，且不含0）
#能满足形如： ab * cde = adb * ce 这样的算式一共有多少种呢？
#请你利用计算机的优势寻找所有的可能，并回答不同算式的种类数。
#满足乘法交换律的算式计为不同的种类，所以答案肯定是个偶数。
#因为 36 * 495 = 396 * 45 = 17820
#类似这样的巧合情况可能还有很多，比如：27 * 594 = 297 * 54
#思路：循环遍历。
#答案：142


n=0
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                for e in range(1,10):
                    if a !=b and a !=c and a !=d and a !=e and b !=c and b !=d and b !=e and c !=d and c !=e and d !=e:
                        if ((a*10+b)*(c*100+d*10+e)) == ((a*100+d*10+b)*(c*10+e)):
                            n=n+1
print(n)