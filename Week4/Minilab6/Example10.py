def is_palindrome(word):
    # convert lovercas
    word = word.lower()
    # check forwards
    return word == word[::-1]

# Want word from user
word = input("Please enter a word: ")

# Check is it palindrome
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
