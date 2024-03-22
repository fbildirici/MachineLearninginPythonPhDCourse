import numpy as np

# Generate values between 0 and 2π
angles = np.linspace(0, 2 * np.pi, 10)

# Compute
sin_values = np.sin(angles)

# Print
for angle, sinus in zip(angles, sin_values):
    print(f"Angle: {angle:.2f} rad, Sine: {sinus:.2f}")
