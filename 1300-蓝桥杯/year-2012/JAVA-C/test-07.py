for i in range(1,21):
    for j in range(1,i):
        for x in range(1,j):
            for y in range(1,x):
                if 1/i+1/j+1/x+1/y==1:
                    print(i,j,x,y,0)