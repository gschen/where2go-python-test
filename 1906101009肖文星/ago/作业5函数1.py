import math
def quadratic(a,b,c):
    x1 = (-b + math.sqrt(b ** 2 - 4 * a*c)) / 2 * a
    x2 = (-b - math.sqrt(b ** 2 - 4 * a*c)) / 2 * a
    print(x1,x2)
quadratic(1,4,4)