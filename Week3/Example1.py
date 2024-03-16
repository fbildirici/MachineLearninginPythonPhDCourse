def calculate_bmi(weight_kg, height_m):
    # BMI formülü
    bmi = weight_kg / (height_m ** 2)
    # BMI değerine göre değerlendirmesi
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obesity"

    return bmi, category
# Örnek yapalim
weight_kg = 70  # kg ağırlık
height_m = 1.75  # metre boy

bmi, category = calculate_bmi(weight_kg, height_m)
print(f"Calculated BMI: {bmi:.2f}, Category: {category}")
