# Bir önceki islemden kalan stringi ele alalim
a = "'araknA nohtyP"

# İlk kelimenin tersini alalim digeri kalsin
kelimeler = a.split(" ")
sonuc = kelimeler[0][::-1] + " " + " ".join(kelimeler[1:])  # İlk kelimenin tersini cevirip geri kalanıyla merge edelim

# Sonucu yazdırma
print(sonuc)
