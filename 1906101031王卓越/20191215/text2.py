low,high=map(int,input().split())
n=[]
s=1
k=1
a=2
y=1
while s<high:
    s=a-1
    for i in range(k):
        s=s*10+a
        a=a+1
        if a==10:
            k=k+1
            a=2
            y=1
            break
        if i==k-1:
            a=y+1
            y=y+1
    if s>low and s<high:
        n.append(s)
n=set(n)
n=sorted(n)
print(n)
    









