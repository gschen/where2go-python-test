a,c,d,b=input().split()
low=False
high=False
a=float(a)
b=float(b)
c=float(c)
d=float(d)
if(a>0 and b>0 and c>0 and d>0):
    if(b<a):
        la="BW-Solid"
    elif(b>a):
        la="R-Hollow"
    else:
        la="R-Cross"
    if(d<a and d<b):
        low="Lower Shadow"
    if(c>a and c>b):
        high="Upper Shadow"
    if(low and high):
        print(la+" with "+low+" and "+high)
    elif(low):
        print(la + " with " + low)
    elif (high):
        print(la + " with " + high)
    else:
        print(la)