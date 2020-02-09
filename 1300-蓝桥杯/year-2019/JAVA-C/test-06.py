# (思路：按它的位置相应的取到对脚上的数字就可以了)
n,m=map(int,input().split(' '))
l=input().split(' ')
L=[]
k=0
nn=n
for i in range(m):
    while nn>0:
        if k>n:
            break
        L.append(l[(nn-1)*m+k])
        nn-=1
    k+=1
    nn=n
print(' '.join(L))