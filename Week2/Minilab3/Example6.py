# İsim listesi tanimla
x = ['Veli BAL', 'Ali AK', 'Hakan YILMAZ', 'İbrahim DEMİR', 'Osman ÇELİK', 'Zeynep TAŞ']

# İsim listesinden sozluk yaratalim
dic = {i+1: name for i, name in enumerate(x)}

# Sonucu yazdiralim
print(dic)
