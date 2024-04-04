from scipy.misc import derivative

# Fonksiyonumuz f(x) = x^3 - 3x + 1
def f(x):
    return x**3 - 3*x + 1

# x=2 noktasında f fonksiyonunun birinci türevi
first_derivative = derivative(f, 2, dx=1e-6, n=1)

# x=2 noktasında f fonksiyonunun ikinci türevi
second_derivative = derivative(f, 2, dx=1e-6, n=2)

(first_derivative, second_derivative)

print(first_derivative)
print(second_derivative)
