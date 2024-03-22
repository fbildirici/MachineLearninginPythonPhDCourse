# sum for evens
sum_even_numbers = 0

# for loop 0-100
for number in range(1, 101):
    # even check
    if number % 2 == 0:
        sum_even_numbers += number

# Print
print(f"The sum of all even numbers between 1 and 100 is: {sum_even_numbers}")
