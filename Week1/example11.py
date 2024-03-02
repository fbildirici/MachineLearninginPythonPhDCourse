# Bir liste verelim
l = ["Ankara", "İstanbul", "İzmir", "Adana"]

# İlgili listede a harfini arayalim
a_sayisi = sum(kelime.lower().count('a') for kelime in l)

# bu harfi aradigimiz ve topladigimiz degiskeni yazdiralim
print(a_sayisi)
