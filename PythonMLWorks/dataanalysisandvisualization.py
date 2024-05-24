import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# Veriyi yükleyelim
data = pd.read_csv(r'C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Homework\ML\pokemon.csv')

# Veri Analizi
description = data.describe()

# Veri hakkında genel bilgi edinelim
info_buffer = StringIO()
data.info(buf=info_buffer)
info_data = info_buffer.getvalue()
head_data = data.head()

# Sonuçları bir metin dosyasına yazdıralım
with open('pokemon_data_analysis_summary.txt', 'w', encoding='utf-8') as file:
    file.write("Head of the data:\n")
    file.write(head_data.to_string())
    file.write("\n\nInfo about the data:\n")
    file.write(info_data)
    file.write("\n\nData Description:\n")
    file.write(description.to_string())

print("Data analysis summary has been written to pokemon_data_analysis_summary.txt")

# Veri Görselleştirme
# Özelliklerin dağılımını görmek için pairplot
sns.pairplot(data)
plt.savefig('pairplot.png')
plt.show()
