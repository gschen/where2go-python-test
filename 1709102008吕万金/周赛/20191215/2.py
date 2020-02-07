low,high=map(int,input().split(','))
n=len(str(high))
k=len(str(low))
l=[]
for i in range(low,high):
    if n==k:
        c=''
        i=str(i)
        while k>0:
            c=i[k-1]+c
            k-=1
print(c)
    # elif k<n:

