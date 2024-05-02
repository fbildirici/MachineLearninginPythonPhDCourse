import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -3 * x**2 + 7

x = np.linspace(-10, 10, 400)

y = f(x)
#plot create
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = -3x² + 7')
plt.title('Plot of the function y = -3x² + 7')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
