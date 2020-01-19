l = ['0','1','2','5','6','8','9']
l1 = ['0','1','2','5','9','8','6']
l2 = []
l3 = []
for a,o in zip(l[1:],l1[1:]):
    for b,p in zip(l,l1):
        for c,q in zip(l,l1):
            for d,r in zip(l,l1):
                if (int(a+b+c+d)-int(r+q+p+o))//100 == 2:
                    l2.append((a+b+c+d,r+q+p+o))
                if (int(r+q+p+o)-int(a+b+c+d))//100 == 8:
                    l3.append((a+b+c+d,r+q+p+o))
for x in l2:
    for y in l3:
        if int(y[1])-int(y[0])-(int(x[0])-int(x[1])) == 558:
            print(x[0])
            break


