# Bir sozluk yapisi kuralim icerigimizle
dic = {"kırmızı": "red", "yeşil": "green", "mavi": "blue"}

# Yabanci dil ingilizce turkce sozluk yaratalim
english_turkish_dic = {value: key for key, value in dic.items()}

# Sozlugun icerigini yazdiralim
print(english_turkish_dic)


# EKSTRA - EKSTRA
# EKSTRA olarak her birinin karsiligini yazdirmayi deneyelim
english_turkish_dic = {"red": "kırmızı", "green": "yeşil", "blue": "mavi"}

# Deneme
for english_word, turkish_word in english_turkish_dic.items():
    print(f"{english_word} means {turkish_word} in Turkish.")
