'''
6.标题：兰顿蚂蚁
'''
dir=[[-1,0],[0,1],[1,0],[0,-1]]#上左下右
m,n=map(int,input().split())
ls=[]
for i in range(m):#m排
    ls_a=list(map(int,input().split()))
    ls.append(ls_a)
for i in range(m):
    for j in range(n):
        if ls[i][j]==0:
            ls[i][j]=False
        else:
            ls[i][j]=True
x=int(input())
y=int(input())
c=input()
k=int(input())
current=0
if c=="U":
    current=0
elif c=="D":
    current=2
elif c=="L":
    current=3
else:
    current=1
for i in range(k):
    if ls[x][y]:
        current+=1
        current=current%4
        ls[x][y]=bool(1-ls[x][y])
        x+=dir[current][0]
        y+=dir[current][1]
    else:
        current-=1
        current=(current+4)%4
        ls[x][y]=bool(1-ls[x][y])
        x+=dir[current][0]
        y+=dir[current][1]
print("{},{}".format(x,y))
