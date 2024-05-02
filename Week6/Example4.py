import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 500)
y = np.cos(2 * np.pi * x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, 'b-', label='Cosine curve')  # Blue line for the cosine curve

min_index = np.argmin(y)
min_x = x[min_index]
min_y = y[min_index]

plt.annotate('Yerel Minimum', xy=(min_x, min_y), xytext=(min_x + 0.5, min_y + 0.5),
             textcoords="offset points", arrowprops=dict(facecolor='red', arrowstyle='->'))
plt.title('Cosine Wave Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0, 5)
plt.ylim(-2, 2)
plt.grid(True)
plt.legend()
plt.show()
