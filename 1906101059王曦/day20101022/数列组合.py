list = ['a','b','c','d']
for x in list:
    for y in list:
        for z in list:
            if x!=y and x!=z and y!=z:
                print(x+y+z)