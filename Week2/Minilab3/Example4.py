# Notlari verelim
final = {"074": 78, "060": 88, "214": 77, "663": 66, "142": 83, "541": 55, "742": 75, "117": 69}

# Toplam ve ögrenci sayisini alalim
total_score = sum(final.values())
number_of_students = len(final)

# Ortalama notu dusunelim
class_average = total_score / number_of_students

# Sonucu yazdiralim
print(class_average)
