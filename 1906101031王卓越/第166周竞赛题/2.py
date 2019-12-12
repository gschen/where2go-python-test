groupSizes=input()
groupSizes=list(eval(groupSizes))
n=[]
for i in range(len(groupSizes)):
    if groupSizes[i] not in groupSizes[:i]:
        s=[]
        for k in range(i,len(groupSizes)):
            if groupSizes[i]==groupSizes[k]:
                s.append(k)
                if len(s)%groupSizes[i]==0:
                    n.append(s[-groupSizes[i]:])
                continue
            if groupSizes[i]==1 and i==k:
                s.append(i)
                n.append(s[-1:])
                break 
print(n)

    
