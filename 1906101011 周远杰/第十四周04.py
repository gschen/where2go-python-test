#给定一个正整数N，将其表示为数字1,2,5,11相加的形式输出。 要求上述数字出现的总次数最少(每个数字可以重复使用)。
#输入说明:一个正整数N (N<= 10000)。
#输入：21
#输出：11
#	   5
#	   5

def zhou(x):
    if x>=11:
        print(11)
        return zhou(x-11)
    elif 5<=x<11:
         print(5)
         return zhou(x-5)
    elif 2<=x<5:
         print(2)
         return zhou(x-2)
    elif x==1:
        print(1)
        return zhou(x-1)
N=int(input())
zhou(N)