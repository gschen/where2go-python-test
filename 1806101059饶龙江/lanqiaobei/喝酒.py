for i in range(5,21):
    for j in range(4,i):
        for x in range(3,j):
            for y in range(2,x):
                if (1/i)+(1/j)+(1/x)+(1/y)==1:
                    print(i,j,x,y)
