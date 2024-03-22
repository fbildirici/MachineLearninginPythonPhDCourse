import numpy as np

# Our matrixs - The Matrix is everywhere. It is all around us.
A = np.array([[1, 5, 9],
              [4, 3, 2],
              [0, 2, 7]])
b = np.array([[6],
              [1],
              [8]])
c = np.array([[3],
              [2],
              [9]])

AtA = np.dot(A.T, A)

bcT = np.dot(b, c.T)

calc_AtA = 0.06 * AtA

matrixresult = calc_AtA - bcT

print(matrixresult)
