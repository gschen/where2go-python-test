m=['a','b','c']
for i in range(0,3):
    for o in range(0,3):
        for p in range(0,3):
            if i!=0 and o!=0 and p!=2 and i!=o!=p:
                print('{}对x,{}对y，{}对z'.format(m[i],m[o],m[p]))
#9