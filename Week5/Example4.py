from scipy.optimize import newton
import numpy as np

# Fonksiyon tanimi f(x) = x^3 - 3x + 1
def f(x):
    return x**3 - 3*x + 1

# Derivative tanimlama of f, f'(x) = 3x^2 - 3
def f_prime(x):
    return 3*x**2 - 3

critical_point = newton(f_prime, 0)

minimum_value = f(critical_point)

(critical_point, minimum_value)

print(critical_point)
print(minimum_value)