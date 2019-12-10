a3,a2,a1,a0=map(int,input().split())
a,b=map(float,input().split())
f = a3*(a**3)+a2*(a**2)+a1*a+a0
m = a3*(b**3)+a2*(b**2)+a1*b+a0
while True:
    if f*m < 0:
        n =(a+b)/2
        g = a3*(n**3)+a2*(n**2)+a1*n+a0
        if g == 0:
            print("%.2f"%n)
        if g*f > 0:
            a = n
            f = a3*(n**3)+a2*(n**2)+a1*n+a0
            m = a3*(b**3)+a2*(b**2)+a1*b+a0
            if f*m<0:
                n =(a+b)/2
                print("%.2f"%n)
        if g*f < 0:
            b = n
            f = a3*(a**3)+a2*(a**2)+a1*a+a0
            m = a3*(b**3)+a2*(b**2)+a1*b+a0
            if f*m<0:
                n = (a+b)/2
                print("%.2f" % n)
        else:
            print("%.2f" % n)



