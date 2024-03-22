import numpy as np

# Define the matrixs a, b, c, and d
a = np.array([[1, 5, 9],
              [4, 3, 2],
              [0, 2, 7]])
b = np.array([[5],
              [3],
              [4]])
c = np.array([[4, 5],
              [6, 9]])
d = np.array([[2],
              [1]])

# vertical placement
c_underneath = np.vstack((c, np.zeros((1, c.shape[1]))))
d_underneath = np.vstack((d, np.zeros((1, d.shape[1]))))

# Construct E a,b normal c and d underneath horizontal
E = np.hstack((a, b, c_underneath, d_underneath))

# Print
print(E)
