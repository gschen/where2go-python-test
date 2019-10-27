"""
14、	本题要求对任意给定的正整数N，求方程X2+Y2=N的全部正整数解。给
定的N<=10000,如果有解请输出全部解，如果无解请输出No Solution。
"""
aa = True
n = int(input("请输入一个数字："))
for i in range(1,101):
    for m in range(1,101):
        if n == i**2+m**2 and i <m:
            print(i,m)
            aa = False
if aa == True:
    print("No Solution.")
