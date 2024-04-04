from scipy.linalg import solve
import numpy as np

# Bu variableların katsayılarına bakalım
coefficients = np.array([[5.3, 1.2, -2.6],
                         [6.1, -2.3, 6.2],
                         [2.2, -4.7, -3.6]])

# Constantsları yazalim
constants = np.array([2.3, 1.9, 3.6])

# Scipy kullanarak degerleri hesaplamayi deneyelim
solution = solve(coefficients, constants)
solution

print(solution)