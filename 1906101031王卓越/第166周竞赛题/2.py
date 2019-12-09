groupSizes=input()
groupSizes=list(eval(groupSizes))
n=[]
a=0
for i in range(len(groupSizes)):
    if groupSizes[i]!=a:
        a=groupSizes[i]
        s=[i]
        for k in range(i+1,len(groupSizes)):
            if groupSizes[i]==groupSizes[k]:
                s.append(k)
                if len(s)%groupSizes[i]==0:
                    n.append(s[-groupSizes[i]:])
                continue
            if groupSizes[i]==1:
                s.append(i)
                n.append(s[-1:])
                break 
            if groupSizes[0]==1:
                n.append([0])
print(n)

    
