import numpy as np
import matplotlib.pyplot as mat
x = np.arange(30)
mat.xlim((0, 100))
mat.ylim((0, 100))
def f(x):
    y = 2*x
    return y
mat.plot(x, f(x), 'b-', linewidth=3, label="f(x)")
mat.text(10,20,'f(x)',size=13)
mat.legend(['f(x)'], loc='upper left')
mat.show()