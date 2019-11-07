import numpy as np
# print(np.ones(4))
# print(np.zeros((3,4)))
#
# a = np.zeros((4,6))
# b = np.zeros(3)
# print(a.shape)
# print(a.ndim)
# print(a.size)


# print(np.empty((2,2,2)))
#
# print(np.array([[1,2,3],[4,5,6]]))
# print(np.arange(1,15,1.5))

#print(np.linspace(0,4/3,6))

#print(np.random.rand(3,4))
#print(np.random.randn(3,4))


#%matplotlib inline
# import matplotlib.pyplot as plt
# plt.hist(np.random.rand(100000), normed=True, bins=100, histtype="step", color="blue", label="rand")
# plt.hist(np.random.randn(100000), normed=True, bins=100, histtype="step", color="red", label="randn")
# plt.axis([-2.5, 2.5, 0, 1.1])
# plt.legend(loc = "upper left")
# plt.title("Random distributions")
# plt.xlabel("Value")
# plt.ylabel("Density")
# plt.show()

#print(np.fromfunction(lambda i,j:i+j,(4,4)))
# d = np.arange(1,5,dtype=np.complex64)
# print(d.dtype,d.itemsize)
#
# f = np.array([[1,2],[1000,2000]],dtype=np.int32)
# print(f.data)

f = np.arange(9)
g=f.reshape((3,3))
print(g)
print(np.ravel(g))
