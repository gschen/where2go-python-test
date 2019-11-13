#输出华氏-摄氏温度转换表
l,u = map(int,input('请输入两个数：').split())
if l>u:
    print('Invalid')
else:
    print('fahr celsius')
    f = l
    while l<=f<=u:
        c = 5*(f-32)/9
        print(f,'  ''%.1f'% c)
        f += 2
