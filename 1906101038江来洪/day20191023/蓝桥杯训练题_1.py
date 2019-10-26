list = ['a','b','c','d']
for a in list:
    for b in list:
        for c in list:
            if a!=b and b!=c and a!=c:
                print(a+b+c)
