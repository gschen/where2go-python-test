
def quadratic(a,b,c):
    delta=b**2-4*a*c
    if delta>=0:
        s=(abs(delta))**0.5
        result_1=(-b-s)/(2*a)
        result_2=(-b+s)/(2*a)
        return [result_1,result_2]
    else:
        return "无解"
print(quadratic(1,9,3))