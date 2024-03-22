import random

# Generate random nums
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

# Calculate correct
correct_answer = num1 * num2

# Ask user
user_answer = int(input(f"What is {num1} * {num2}? "))

# Check
if user_answer == correct_answer:
    print("Correct! Well done.")
else:
    print(f"Wrong. The correct answer is {correct_answer}.")
