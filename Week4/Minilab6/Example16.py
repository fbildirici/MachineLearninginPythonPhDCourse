# frequency
sentence = "Man is still the most extraordinary computer of all. - John F. Kennedy"

# Convert lovercase
filtered_sentence = ''.join(filter(str.isalpha, sentence)).lower()

# Frequency calculation
frequency = {}
for letter in filtered_sentence:
    if letter in frequency:
        frequency[letter] += 1
    else:
        frequency[letter] = 1

# Print
for letter, freq in frequency.items():
    print(f"'{letter}': {freq} times")
