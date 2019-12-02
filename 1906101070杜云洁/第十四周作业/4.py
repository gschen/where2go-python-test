a=int(input())
b=a
c=[11,5,2,1]
c2=[]
for i in c:
    while a >=i:
        a -=i
        c2.append(i)
        c2.append('+')
del c2[-1]
print(b,'=',end='')
for d in c2:
    print(d,end='')