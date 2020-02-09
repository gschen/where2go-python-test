import numpy as np
n=int(input())
lis6=[]
for i in range(0,n):
    a=list(input())
    l=len(a)
    zu=int(l/6)
    lis3=[0,0,0,0,0,0]
    lis3=np.array(lis3)
    for i in range(0,zu):
        lis1=[]
        lis1=a[0:6]
        a=a[6:]
        lis2=[]
        for i in lis1:
            lis2.append(ord(i))
        lis3 += np.array(lis2)
    lis5=[]
    for i in a:
        lis5.append(ord(i))
    while len(lis5)<6:
        lis5.append(0)
    lis5=np.array(lis5)
    lis3=lis3+lis5
    lis3=list(lis3)
    lis4=[]
    for i in lis3:
        zfc = ''
        zfc+=str(i)
        cd=len(zfc)
        while cd>1:
            sums=0
            for j in zfc:
                sums+=int(j)
            cd=len(str(sums))
            zfc=str(sums)
        lis4.append(sums)
        s=''
        for i in lis4:
            s+=str(i)
    lis6.append(s)
for i in lis6:
    print(i)







