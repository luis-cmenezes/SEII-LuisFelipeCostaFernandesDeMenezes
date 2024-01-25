import numpy as np

a = np.array([[7,8,9,10,11,12,13], [17,18,19,20,21,22,23]])
print(a)

print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))

print(a.mean())
print(a.mean(axis=0))
print(a.mean(axis=1))

print(a.var())
print(a.std())

print(a.min())
print(a.max())