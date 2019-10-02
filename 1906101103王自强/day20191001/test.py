# -*-_ coding:UTF-8 -*-
#求三角形的面积
while True:
    a=float(input('请输入三角形的一边长;'))
    b=float(input('请输入三角形的二边长;'))
    c=float(input('请输入三角形的三边长;'))
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print('三角形的面积为；%0.2f'%(area))