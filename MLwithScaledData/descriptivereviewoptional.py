import pandas as pd

# Veriyi yükleyelim
file_path = r'C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Homework\ML\final_pokemon.csv'
data = pd.read_csv(file_path)

# Betimsel istatistikleri hesaplayalım
descriptive_stats = data.describe(include='all')

# Dosyaya kaydedelim
output_file_path = 'descriptive_statistics.txt'
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write("Veri Seti Betimsel İstatistikleri:\n")
    f.write(descriptive_stats.to_string())

# Konsola da yazdıralım
print("Veri Seti Betimsel İstatistikleri:")
print(descriptive_stats)
