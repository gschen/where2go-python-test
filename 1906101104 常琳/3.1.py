sum=0
m,n=2,1
for i in range(20):
    sum=sum+m/n
    m=m+n
    n=m-n
print(sum)

