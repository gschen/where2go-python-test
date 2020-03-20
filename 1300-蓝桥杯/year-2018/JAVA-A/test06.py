'''
6、标题：螺旋折线
'''
x=int(input())
y=int(input())
res=0
if abs(x)>abs(y):
    p=x
    q=1
else:
    p=y
    q=2
res=4*abs(p)*(abs(p)-1)
if q==1 and x<0:
    res+=y-x
elif q==1 and x>=0:
    res=-7*y-x
else:
    res+=3*y+x
print(res)