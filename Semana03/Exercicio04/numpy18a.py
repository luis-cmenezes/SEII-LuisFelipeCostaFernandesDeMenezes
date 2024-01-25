import numpy as np

data = np.loadtxt('spambase.csv', delimiter=",", dtype=np.float32)
data = np.genfromtxt('spambase.csv', delimiter=",", dtype=np.float32)