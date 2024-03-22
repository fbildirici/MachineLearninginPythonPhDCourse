# sequence
sequence = [89, 5, 4, 101, 23, 11, 178, 241, 2, 17]

# largest definition
largest = sequence[0]

# iteration starts second elements
for number in sequence[1:]:
    # find largest
    if number > largest:
        largest = number

# Print
print(f"The largest element in the sequence is: {largest}")
