# Dictionary yapisi tanimlayalim
midterm = {"11386074": 56, "13478060": 66, "13147214": 87}
final = {"11386074": 78, "13478060": 88, "13147214": 77}
students = {"Kazım Gök": "11386074", "Ahmet KILIÇ": "13478060", "Veli Demir": "13147214"}

# Ahmet Kılıç icin bilgi bulalim
ahmet_id = students["Ahmet KILIÇ"]

# Ahmet Kılıç icin sinav notlarini alalim
ahmet_midterm_score = midterm[ahmet_id]
ahmet_final_score = final[ahmet_id]

# Ahmet Kılıç için bu notlardan ortalama hesaplayalim
ahmet_average_score = (ahmet_midterm_score + ahmet_final_score) / 2

# Ortalamayı yazdırıyoruz
print(ahmet_average_score)
