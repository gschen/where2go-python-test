#dict={"li":18,"wang":50,"zhang":20,"sun":22}
dict = {"li":18,"wang":50,"zhang":20,"sun":22}
m="li"
for key in dict.keys():
    if dict[m]<dict[key]:
        m=key
        print('%s,%d'%(m,dict[m]))


