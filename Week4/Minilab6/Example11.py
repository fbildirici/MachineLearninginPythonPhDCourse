def are_anagrams(word1, word2):
    word1, word2 = word1.lower(), word2.lower()

    count1, count2 = {}, {}
    for letter in word1:
        if letter in count1:
            count1[letter] += 1
        else:
            count1[letter] = 1
    for letter in word2:
        if letter in count2:
            count2[letter] += 1
        else:
            count2[letter] = 1
    return count1 == count2
word1 = input("Please enter the first word: ")
word2 = input("Please enter the second word: ")
if are_anagrams(word1, word2):
    print(f"'{word1}' and '{word2}' are anagrams.")
else:
    print(f"'{word1}' and '{word2}' are not anagrams.")
