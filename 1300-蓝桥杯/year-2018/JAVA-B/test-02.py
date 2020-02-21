r=1000
count=0
b=0
for i in range(1000,0,-1):
    y=0
    while i*i+y*y<=r*r:
        y+=1
    y-=1
    count+=i*(y-b)
    b=y
print(count*4)