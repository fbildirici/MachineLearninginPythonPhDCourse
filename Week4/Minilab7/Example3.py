import numpy as np

# Matrix - Blue or Red Pill
A = np.array([[2, 5, 14],
              [7, 9, 12],
              [8, 2, 6]])

# NEO What truth?
elements_greater_than_5 = A[A > 5]

# Print
print("Elements of the matrix greater than 5:", elements_greater_than_5)
