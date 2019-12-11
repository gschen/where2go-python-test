'''
本题目要求计算下列分段函数f(x)的值：f(x)=0 x=0    f(x)=1/x x-=0

输入格式:
输入在一行中给出实数x。
输出格式:
在一行中按“f(x) = result”的格式输出，其中x与result都保留一位小数。
'''



x = float(input())
if x != 0:
    print("sum=",1 / x)
else:
    print("0")


