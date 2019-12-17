def raw(a,b,c):
    import math
    l=math.sqrt(b**2-4*a*c)
    z=(-b+l)/(2*a)
    p=(-b-l)/(2*a)
    return z , p
a,b,c=map(int,input("分别输入a,b,c:").split())
print(raw(a,b,c))