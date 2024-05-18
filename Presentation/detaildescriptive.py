import pandas as pd
import numpy as np

# Dosya yolunu belirtin
file_path = r"C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Presentation\pokemon.csv"

# CSV dosyasını oku
pokemon_df = pd.read_csv(file_path)

# Tanımlayıcı istatistikler hesaplama
descriptive_stats = pokemon_df.describe(include='all')

# Veri tiplerini belirle
data_types = pokemon_df.dtypes

# Eksik değerleri hesapla
missing_values = pokemon_df.isnull().sum()

# Benzersiz değer sayısını hesapla
unique_values = pokemon_df.nunique()

# Ek istatistikler hesaplama
numeric_columns = pokemon_df.select_dtypes(include=[np.number]).columns
extra_stats = pd.DataFrame(index=numeric_columns)
extra_stats['Range'] = pokemon_df[numeric_columns].max() - pokemon_df[numeric_columns].min()
extra_stats['Variance'] = pokemon_df[numeric_columns].var()
extra_stats['Skewness'] = pokemon_df[numeric_columns].skew()
extra_stats['Kurtosis'] = pokemon_df[numeric_columns].kurtosis()
extra_stats['Median'] = pokemon_df[numeric_columns].median()

# Özet istatistikler DataFrame'ini oluşturma
summary_stats = pd.DataFrame({
    'Data Type': data_types,
    'Missing Values': missing_values,
    'Unique Values': unique_values
})

# Tanımlayıcı istatistikler ve ek istatistikleri summary_stats DataFrame'e ekle
summary_stats = summary_stats.join(descriptive_stats.transpose())
summary_stats = summary_stats.join(extra_stats)

# Özet istatistikleri yazdır
print(summary_stats)

# Özet istatistikleri Excel dosyasına kaydet
output_path = r"C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Presentation\summary_statistics.xlsx"
summary_stats.to_excel(output_path, index=True)

print(f"Summary statistics saved to {output_path}")
