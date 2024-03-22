import random

def roll_double_dice():
    # randint 1
    die1 = random.randint(1, 6)
    # randint 2
    die2 = random.randint(1, 6)
    return die1, die2

# rolling function
die1, die2 = roll_double_dice()

# Print
print(f"First die roll: {die1}, Second die roll: {die2}")
print(f"Total: {die1 + die2}")
