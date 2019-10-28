list1 = ('x','y','z')
for a in list1:
    for b in list1:
        for c in list1:
            if a!=b and b!=c and c!=a and a!='x' and c!='x'and c!='z':
                print('a和%s,b和%s，c和%s' % (a,b,c))
