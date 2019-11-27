L = ['a', 'b', 'c', 'd']
for x in range(0, 4):
    for y in range(0, 4):
        for z in range(0, 4):
            if x != y and y != z and z != x:
                print('{}{}{}'.format(L[x], L[y], L[z]))


