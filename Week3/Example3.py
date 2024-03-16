def find_vowels(text):
    # Sesli harfleri ögretelim
    vowels = 'aeiouAEIOU'
    # Gelen metindeki sesli harfleri alacak bir liste yaratalim
    found_vowels = [char for char in text if char in vowels]
    return found_vowels

# Örnek yapalim:
text = "Good morning, everyone, and welcome to 'Science and Society.' I'm Dr. Sheldon Cooper, BS, MS, MA, PhD, And ScD. OMG"
print(find_vowels(text))
