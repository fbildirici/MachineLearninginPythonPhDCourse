def count_vowels(word):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    for char in word:
        if char in vowels:
            vowel_count += 1
    return vowel_count

# Want word from user
word = input("Kelimeleri görelim: ")

# Print
vowel_count = count_vowels(word)
print(f"The total number of vowels in '{word}' is: {vowel_count}")
