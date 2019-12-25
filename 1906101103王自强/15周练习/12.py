l=list(map(int,input().split(' ')))
sum=0
box=[]
for i in l:
    sum+=i
averge=sum/len(l)
for j in l:
    if j>averge:
        box.append(str(j))
print(' '.join(box))