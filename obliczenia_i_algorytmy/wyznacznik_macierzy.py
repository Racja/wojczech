import random
import numpy as np

random.seed()

A_matrix = np.random.rand(3, 3) * 10

det = np.linalg.det(A_matrix)

print(A_matrix, "\n")
print(det)
