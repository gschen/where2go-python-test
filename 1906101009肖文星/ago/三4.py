'''本题要求对任意给定的正整数N，求方程X2+Y2=N的全部正整数解。给定的N<=10000,如果有解请输出全部解，如果无解请输出No Solution。'''
N = int(input())
m = 0
if N > 10000 or N <= 0 :
    print('输入的N值超出给定范围.')
else:
    for x in range(1,N):
        for y in range(1,N):
            if x**2 + y**2 == N:
                print('X={},Y={}'.format(x,y))
                if x**2 + y**2 != N:
                    m +=1
                if m ==N-1:
                    print('No Solution')