x,y =map(str,input().split(":"))
a = "AM"
b = "PM"
x = int(x)
y = int(y)
if x<12:
    print("%d:%d %s"%(x,y,a))
if x==12:
    print("%d:%d %s"%(x,y,b))
if x > 12:
    x = x%12
    print("%d:%d %s" %(x,y,b))
