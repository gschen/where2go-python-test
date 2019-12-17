#输出三角形面积和周长
a,b,c = map(int,input('请分别输入三角形的三边长：').split())
if a+b<c or a+c<b or b+c<a:
    print('These sides do not correspond to a valid triangle')
else:
    C = a+b+c
    s = C/2
    S = (s*(s-a)*(s-b)*(s-c))**0.5
    print('area = %s'% '%.2f'% S, ';', 'perimeter = %s'% '%.2f'% C)