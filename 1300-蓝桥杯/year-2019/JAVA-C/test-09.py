
k=input()
a=input()
a1=[]
a2=[]
a3=[]
a4=[]
n=0
s=list(map(chr, range(ord('a'), ord('z') + 1)))+list(map(chr, range(ord('A'), ord('Z') + 1)))
for i in range(len(a)):
    if a[i:i+5]=='Alice' and a[i-1] not in s and a[i+5] not in s:
        a1.append(i)
        a2.append(i+5)
    if a[i:i+3]=='Bob' and a[i-1] not in s and a[i+3] not in s :
        a3.append(i)
        a4.append(i+3)
for ii in a1:
    for iii in a4:
        if ii-iii<=k+1 and ii-iii>0:
            n+=1
for iiii in a2:
    for iiiii in a3:
        if iiiii-iiii<=k+1 and iiiii-iiii>0:
            n+=1
print(n)

