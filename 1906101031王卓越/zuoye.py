def quadratic(a,b,c):
    import math
    z=b**2
    k=4*a*c
    s=z-k
    r=math.sqrt(s)
    i=(-b+r)/(2*a) 
    l=(-b-r)/(2*a)
    return i,l
a,b,c = map(int,input('请输入：').split())
print(quadratic(a,b,c))
