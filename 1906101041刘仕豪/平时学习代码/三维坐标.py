from matplotlib import pyplot
import numpy
from mpl_toolkits.mplot3d import Axes3D
f = pyplot.figure()
a = Axes3D(f)
X = numpy.arange(8)
Y = numpy.arange(8)
X, Y = numpy.meshgrid(X, Y)
R = numpy.sqrt(X)
Z = numpy.sin(R)
a.plot_surface(X, Y, Z, rstride=2, cstride=2, cmap='twilight_r')
pyplot.show()