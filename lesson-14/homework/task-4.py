import numpy as np

# define the coefficients of matrix as A
A = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])

# define the constants as B
B = np.array([12, -5, 15])\

# use numpy.linalg.solve
X = np.linalg.solve(A, B)

#print the results
print(f"[I1, I2, I3] = {X}")