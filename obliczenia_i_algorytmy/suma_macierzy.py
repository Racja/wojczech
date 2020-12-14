import random
import numpy as np

random.seed()

A_matrix = np.random.rand(128, 128) * 100
B_matrix = np.random.rand(128, 128) * 100

sum_matrix = A_matrix + B_matrix

print(A_matrix, "\n")
print(B_matrix, "\n")
print(sum_matrix)
