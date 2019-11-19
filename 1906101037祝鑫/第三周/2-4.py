#本题要求对任意给定的正整数N，求方程X​2​​+Y​2​​=N的全部正整数解。给定的N<=10000,如果有解请输出全部解，如果无解请输出No Solution。

n = int(input())
m = 0
if n > 10000 or n < 0 :
    print('输入的N值超出给定范围.')
else:
    for x in range(0,n):
        for y in range(0,n):
            if x**2 + y**2 == n:
                print('X={},Y={}'.format(x,y))
            if x**2 + y**2 != n:
                m +=1
                if m >= n**2:
                    print('No Solution')