# Sayilari girelim
numbers = [878.741, 7.2156e2, 16.8]

# İstenen formatlarda biçimlendiriyoruz
formatted_numbers = [
    "{:.0f}".format(numbers[0]),  # Tamsayiyacevirdik
    "{:.4f}".format(numbers[1]),  # Float
    "{:05.0f}".format(numbers[2])  # Bes haneli tam sayi
]

# Sonuclari yazdir
for num in formatted_numbers:
    print(num)
