# Sayilarimizi ekleyelim
numbers = [1.3457899e2, 13, 1478]

# Formatlayalim
formatted_number1 = "{:.3f}".format(numbers[0])  # Ondalik 3 hane
formatted_number2 = "{:05d}".format(numbers[1])  # En az 5 hane tam sayi
formatted_number3 = "{:.3f}".format(numbers[2])  # Ondalik 3 hane sifirli

# islenmis halini  basalim
print(formatted_number1)
print(formatted_number2)
print(formatted_number3)
