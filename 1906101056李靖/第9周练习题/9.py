l=['a','b','c']
for f in range(0,3):
    for g in range(0,3):
        for h in range(0,3):
            if f!=0 and h!=2 and h!=0 and f!=g and f!=h and g!=h:
                print('x对{},y对{},z对{}'.format(l[f],l[g],l[h]))