import numpy as np

A = np.array([[1,1],[1.5,4]])
B = np.array([2200,5050])

X = np.linalg.inv(A).dot(B)
print(X)

x = np.linalg.solve(A,B)
print(x)