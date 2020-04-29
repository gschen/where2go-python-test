n=int(input())
# print('1')
res=[1]
print(res[0])
l=[]
for i in range(n-1):
    for x in range(len(res)):
        print(res[0])
        if x-1==0:            
            l.append(res[x])
            continue
        l.append(int(res[x]+res[x-1]))
        print(l)
    print(''.join,l)
    res=l




