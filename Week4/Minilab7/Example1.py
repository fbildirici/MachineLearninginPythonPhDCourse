import numpy as np

# Our matrix NEO
A = np.array([[2, 5, 14],
              [7, 9, 12],
              [8, 2, 6]])
B = np.array([[47],
              [3],
              [11]])

# multiply
AB = np.dot(A, B)

print(AB)