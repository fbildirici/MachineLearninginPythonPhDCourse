from scipy import optimize as opt

# Define the function
def f(x):
    return x**4 + 3*(x - 2)**3 - 15*x**2 + 1

# Brent metodu kullan
result = opt.minimize_scalar(f, method='Brent', bracket=(0, 6))

print(result)