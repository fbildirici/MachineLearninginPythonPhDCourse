# Sozluk yapisi tanimlayalim
dic = {"kırmızı": "red", "yeşil": "green", "mavi": "blue"}

# Zip yapisini kullanalim
english_turkish_dic = dict(zip(dic.values(), dic.keys()))

# Sonucu gorelim
print(english_turkish_dic)



