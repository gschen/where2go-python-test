a,b,c=map(int,input().split())
if a+b>c and a+c>b and b+c>a:
    s=(a+b+c)/2
    l=s*2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print("area={:.2f};perimeter={:.2f}".format(area,l))