import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 500)

f_t = np.exp(-t) * np.cos(2 * np.pi * t)

# Create the graph
plt.figure(figsize=(8, 5))
plt.plot(t, f_t, label='f(t) = $e^{-t} \cos(2\pi t)$')
plt.title('Damped Oscillation')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid(True)
plt.legend()
plt.show()
