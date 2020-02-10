'''
5.标题：绳圈
'''
f=[[0]*101]*101
f[1][1]=1
for i in range(2,len(f)):
    for j in range(1,i+1):
        f[i][j]=(f[i-1][j-1]+f[i-1][j]*(i-1)*2)/(2*i-1)
max=-1
ans=-1
for i in range(1,len(f[0])):
    if f[100][i]>max:
        max=f[100][i]
        ans=i
print(ans)