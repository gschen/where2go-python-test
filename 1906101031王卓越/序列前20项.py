from fractions import Fraction
x=2
y=1
s=0
k=1
for i in range (0,20):
    z=x/y
    s=z+s
    x=x+y
    p=y
    y=k+y 
    k=p
    #p=map(Fraction,l)
    #print(p)
    #print(x)
print(s)