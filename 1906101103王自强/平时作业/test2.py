def findmaxmin(l):
    if l!=[]:
        (max,min)=(l[0],l[0])
        for i in l:
            if i>max:
                max=i
            if i<min:
                min=i
            return (max,min)