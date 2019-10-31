#求方程X2+Y2=N的全部正整数解
N = int(input('请输入一个数：'))
x = 1
list = []
while True:
    for y in range(1,x+1):
        s = x**2+y**2
        if s == N:
            print(x,y)
            list.append((x,y))
    if x**2>N:
        break
    x += 1
if len(list) == 0:
    print('No Solution')