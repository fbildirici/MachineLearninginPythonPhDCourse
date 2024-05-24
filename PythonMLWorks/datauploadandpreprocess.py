import pandas as pd
from io import StringIO

# Veriyi yükleyelim
data = pd.read_csv(r'C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Homework\ML\pokemon.csv')

# İlk birkaç satırı görelim
head_data = data.head()

# Veri hakkında genel bilgi edinelim
info_buffer = StringIO()
data.info(buf=info_buffer)
info_data = info_buffer.getvalue()

# Sonuçları bir metin dosyasına yazdıralım
with open('pokemon_data_summary.txt', 'w', encoding='utf-8') as file:
    file.write("Head of the data:\n")
    file.write(head_data.to_string())
    file.write("\n\nInfo about the data:\n")
    file.write(info_data)

print("Data summary has been written to pokemon_data_summary.txt")
