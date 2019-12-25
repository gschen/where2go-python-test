l=map(int,input().split(' '))
l2=[]
l1=sorted(l)
for i in l1:
    l2.append(str(i))
print('->'.join(l2))
