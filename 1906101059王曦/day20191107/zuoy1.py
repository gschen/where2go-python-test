#解一元二次方程
import math
def quadratic(a,b,c):
    x = math.sqrt(b ** 2 - 4 * a * c)
    if b**2-4*a*c>0:
        print((-b+x)/(2*a),((-b-x)/(2*a)))
    elif b**2-4*a*c==0:
        print(-b/(2*a))
    else:
        print('无解')

quadratic()