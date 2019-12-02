x=1
y=2
sum=0
for i in range(20):
    sum=x/y+sum
    x,y=(x+y),x
    i=i+1
    print(sum)