a,b,c = map(int,input().split())
if a+b<c or a+c<b or b+c<a:
    print('These sides do not correspond to a valid triangle')
else:
    perimeter = a+b+c
    s = perimeter/2
    area =(s*(s-a)*(s-b)*(s-c))**0.5
    print('area = {:.2f};perimeter = {}'.format(area,perimeter))