
L=[]
for i in range(3):
    a=list(map(int,input().split(" ")))
    L.append(a)
count=0
for i in range(3):
    for j in range(3):
        for k in range(3):
            if L[0][i]<L[1][j] and L[1][j]<L[2][k]:
                count+=1
print(count)
