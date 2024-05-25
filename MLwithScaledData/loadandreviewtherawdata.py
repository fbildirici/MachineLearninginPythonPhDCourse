import pandas as pd

# Veriyi yükleyelim
file_path = r'C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Homework\ML\final_pokemon.csv'
data = pd.read_csv(file_path)

# İlk birkaç satırı görüntüleyelim ve dosyaya kaydedelim
output_file_path = 'data_overview.txt'
with open(output_file_path, 'w', encoding='utf-8') as f:
    first_few_rows = data.head().to_string()
    data_info = data.info()

    f.write("Veri setinin ilk birkaç satırı:\n")
    f.write(first_few_rows + "\n\n")
    f.write("Veri Seti Bilgileri:\n")
    data.info(buf=f)  # info'yu dosyaya yazdırmak için buf parametresini kullanıyoruz

# Konsola da yazdıralım
print("Veri setinin ilk birkaç satırı:")
print(first_few_rows)
print("\nVeri Seti Bilgileri:")
data.info()
