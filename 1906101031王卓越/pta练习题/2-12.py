from math import*
a,b,c=map(int,input().split())
if a+b>c and a+c>b and b+c>a:
    s=(a+b+c)/2
    area=sqrt(s*(s-a)*(s-b)*(s-c))
    perimeter=a+b+c
    print('area =  %.2f ; perimeter = %.2f' % (area , perimeter ))
else:
    print('These sides do not correspond to a valid triangle')