import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 14, 100)

y = np.sin(x)

# Draw the figure
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b-', label='Sine curve')  # Blue line
plt.scatter(x, y, color='r')  # Red dots
plt.title('Sine Wave Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
