import math

# our numbers
num1 = 15
num2 = 65

# gcd calculation
gcd_value = math.gcd(num1, num2)

# LCM = (num1 * num2) / GCD
lcm = (num1 * num2) // gcd_value

# Print with expression
print(f"The Least Common Multiple of {num1} and {num2} is: {lcm}")
