import numpy
def mini(points):
    t = 0
    for i in range(len(points)-1):
        t += max(map(abs,points[i+1]-points[i]))
    return t
points =[[1,1],[3,4],[-1,0]]
points = numpy.array(points)
print(mini(points))