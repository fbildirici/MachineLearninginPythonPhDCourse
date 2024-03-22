import math

data = [4, 2, 6, 1, 7, 5, 4, 6, 3, 8, 9, 8, 7, 1, 2]

mean = sum(data) / len(data)

# variance
variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)

standard_deviation = math.sqrt(variance)

# Print
print(f"The standard deviation of the sample is: {standard_deviation}")
