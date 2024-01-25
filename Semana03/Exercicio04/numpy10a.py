import numpy as np

a = np.array([[1,2],[3,4]])
print(a)
b = np.array([[5,6]])
print(b)

c = np.concatenate((a,b))
print(c)

c = np.concatenate((a,b), axis=None)
print(c)

c = np.concatenate((a,b.T), axis=1)
print(c)