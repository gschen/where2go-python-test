def zhou(points):
    a=abs(points[0][0]-points[1][0])
    b=abs(points[0][1]-points[1][1])
    if a>=b :
        print(a)
    else:
        print(b)
zhou(points=[[1,1],[3,4]])