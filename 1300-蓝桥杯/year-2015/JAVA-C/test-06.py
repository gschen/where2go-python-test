w,n,m=input().split()
if eval(n)%eval(w)==0:
    x1=eval(n)//eval(w)-1
else:
    x1=eval(n)//eval(w)
if eval(m)%eval(w)==0:
    x2=eval(m)//eval(w)-1
else:
    x2=eval(m)//eval(w)
y=abs(x1-x2)
x=abs((eval(n)%eval(w)-1)-((eval(m)//eval(w)+1)*eval(w)-(eval(m)%eval(w)))%eval(w))
# print((eval(n)%eval(w)-1))
# print(((eval(m)//eval(w)+1)*eval(w)-(eval(m)%eval(w)))%eval(w))
# print(y)
# print(x)
len=x+y
print(len)
