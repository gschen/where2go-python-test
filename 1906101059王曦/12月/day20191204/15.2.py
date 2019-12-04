#采购员拿错，求支票面额
n = int(input())
for y in range(0,101):
    for f in range(0,101):
        if f*100+y-n==2*y*100+2*f:
            c = 0
            print('%s.%s' % (f,y))
            if c!=0:
                print("no solution")