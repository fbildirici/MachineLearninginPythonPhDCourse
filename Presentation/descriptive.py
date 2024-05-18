import pandas as pd

# Dosya yolunu belirtin
file_path = r"C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Presentation\pokemon.csv"

# CSV dosyasını oku
pokemon_df = pd.read_csv(file_path)

# Tanımlayıcı istatistikleri hesapla
descriptive_stats = pokemon_df.describe(include='all')

# Tanımlayıcı istatistikleri yazdır
print(descriptive_stats)

# Daha detaylı analiz için veri tiplerini kontrol et
print(pokemon_df.dtypes)
