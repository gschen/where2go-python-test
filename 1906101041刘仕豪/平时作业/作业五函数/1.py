import math
def quadratic(a,b,c):
    if a==0:
        raise TypeError('a不能为0')
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
        raise TypeError('Bad operand type')
    detal = math.pow(b,2) - a*c*4
    if detal<0:
        return'无实根'
    x1=(math.sqrt(detal)-b)/(2*a)
    x2=-(math.sqrt(detal)+b)/(2*a)
    return x1,x2
print(quadratic(2,3,1))