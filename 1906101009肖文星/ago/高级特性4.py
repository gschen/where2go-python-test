def xwx(name):
    name1=name.lower()
    name2=name1.capitalize()
    return name2
L1=['adam','LISA','barT']
L2=list(map(xwx,L1))
print(L2)