a,n=map(int,input().split(' '))
box=[]
for i in range(1,n+1):
    x=str(a)
    box.append(x*i)
sum=0
for j in box:
    sum+=int(j)
print(sum)