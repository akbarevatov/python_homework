import numpy as np
# --- Given system of equations ---
# 4x+5y+6z=7
# 3x−y+z=4
# 2x+y−2z=5

# define an array that represents A in AX=B
A = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

#define an array that represents B in AX=B
B = np.array([7, 4, 5])

# use numpy.linalg.solve to solve the system of equations
X = np.linalg.solve(A, B)
print(f"x, y, z = {X}")