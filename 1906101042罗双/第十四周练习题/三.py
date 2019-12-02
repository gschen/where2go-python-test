x=1
y=2
sum=0
for n in range(20):
    sum=x/y+sum
    x,y=(x+y),x
    n=n+1
    print(sum)