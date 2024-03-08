# Sozluk yapilarini olusturalim
dic1 = {"kırmızı": "red", "yeşil": "green", "mavi": "blue"}
dic2 = {"turuncu": "orange", "kahverengi": "brown", "mor": "purple"}

# Guncelleme islemleri
combined_dic = dic1.copy()  # dic1'in snapshotu
combined_dic.update(dic2)  # dic2'nin icerigini icine basiyoruz

# Sonucu yazdir
print(combined_dic)
