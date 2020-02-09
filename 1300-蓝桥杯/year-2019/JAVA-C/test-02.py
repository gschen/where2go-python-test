x=2019
y=324
n=1
while True:
    if y>x:
        x,y=y,x
    x=abs(x-y)
    x,y=y,x
    n+=1
    if x==y:
        break
print(n)