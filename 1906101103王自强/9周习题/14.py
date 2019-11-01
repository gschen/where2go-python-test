n=int(input('请输入一个整数n=：'))
i=1
for x in range(1,101):
    for y in range(1,101):
        if x**2+y**2==n and x<=y:
            print('解为{}，{}'.format(x,y))
            i=0
if i ==1:
    print('No Solution')