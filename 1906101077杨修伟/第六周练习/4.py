n =int(input())
m = False
if (n>0 and n<100):
    for y in range(100):
        for f in range(100):
            if (y-n<0):
                f = f-1
                y = y+100
            if (f*100+y-n == 2*y*100+2*f):
                print("%d,%d"%(y,f))
                m = True
                break
    if (m == False):
        print("N0 Solution",end="")
