'''12、福尔摩斯到某古堡探险，看到门上写着一个奇怪的算式：
ABCDE * ? = EDCBA
他对华生说：“ABCDE应该代表不同的数字，问号也代表某个数字！”
华生：“我猜也是！”
于是，两人沉默了好久，还是没有算出合适的结果来。
请你利用计算机的优势，找到破解的答案。
把 ABCDE 所代表的数字写出来。
答案：21978
'''
def fun(i):
    wan=i//10000
    qian=(i-wan*10000)//1000
    bai=(i-(wan*10000+qian*1000))//100
    shi=(i-(wan*10000+qian*1000+bai*100))//10
    ge=i%10
    result=ge*10000+shi*1000+bai*100+qian*10+wan
    return result
l=[]
for i in range(10000,100000):
    for j in range(1,10):
        wan = i // 10000
        qian = (i - wan * 10000) // 1000
        bai = (i - (wan * 10000 + qian * 1000)) // 100
        shi = (i - (wan * 10000 + qian * 1000 + bai * 100)) // 10
        ge = i % 10
        if wan!=qian and wan!=bai and wan!=shi and wan!=ge and qian!=bai and qian!=shi and qian!=ge and bai!=shi and bai!=ge and shi!=ge and i*j==fun(i):
            print(i,j)