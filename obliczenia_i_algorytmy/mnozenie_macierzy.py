import random
import numpy as np

random.seed()

A_matrix = np.random.rand(8, 8) * 100
B_matrix = np.random.rand(8, 8) * 100

product_matrix = np.matmul(A_matrix, B_matrix)

print(A_matrix, "\n")
print(B_matrix, "\n")
print(product_matrix)
