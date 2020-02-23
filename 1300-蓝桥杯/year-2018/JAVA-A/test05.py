'''
5、标题：递增三元组
'''
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=[0]*n
e=[0]*n
res=0
for i in range(n):
    for j in range(n):
        if a[i]<b[j]:
            d[i]=j+1
            break
for i in range(n):
    for j in range(n):
        if b[i]<c[j]:
            e[i]=j+1
            break
for i in range(n):
    if d[i]!=0:
        for j in range(d[i]-1,n):
            if e[j]!=0:
                res+=n-e[j]+1
print(res)