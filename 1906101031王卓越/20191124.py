x=10
y=90
k=2
for i in range(1,121):
    if i==k or i%6==0 or i%4==0:
        y=y-x
        k=k+2
        if i%4==0:   
            y=y*2
        elif i%6==0:
            k=k+1
            x=x*2
            y=y-x/2

print(y)

