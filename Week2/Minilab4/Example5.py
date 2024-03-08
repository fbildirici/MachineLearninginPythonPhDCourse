# turkce ve ingilizcede olmayan karakterleri yazalim
turkish = 'abcçdefgğhıijklmnoöprsştuüvyz'
nonEnglish = 'çğıöşü'

# İngilizcenin turkceden fazlalari
onlyEnglish = 'qxw'

# utfe getirecek sekilde ingilizcede olmayanlari turkceden cikarip ekstra harfleri ekleyelim
english_alphabet = ''.join(sorted(set(turkish) - set(nonEnglish) | set(onlyEnglish)))

# Sonucu basalim
print(english_alphabet)
