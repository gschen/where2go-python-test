list=['a','b','c','d']
for i in range(0,4):
    for m in range(0,4):
        for n in range(0, 4):
            if i!=m and m!=n and i!=n:
                print('{}{}{}'.format(list[i],list[m],list[n]))
                #1