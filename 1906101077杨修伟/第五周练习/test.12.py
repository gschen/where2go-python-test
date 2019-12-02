a,b,c=map(str,input().split())
a=int(a)
c=int(c)
if b=="+":
    d=int(a+c)
elif b=="-":
    d=int(a-c)
elif b=="*":
    d=int(a*c)
elif b=="/":
    d=int(a/c)
elif b=="%":
    d=int(a%c)
else:
    d="ERROR"
print(d)

