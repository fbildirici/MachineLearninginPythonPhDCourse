import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from scipy.stats import zscore

# Veriyi yükleyelim
data = pd.read_csv(r'C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Homework\ML\pokemon.csv')

# Sütun adlarını kontrol edelim
print(data.columns)

# Kategorik verileri sayısallaştırma (one-hot encoding)
if 'Type 1' in data.columns and 'Type 2' in data.columns:
    data = pd.get_dummies(data, columns=['Type 1', 'Type 2'], drop_first=True)
else:
    print("Specified columns are not in the dataset")

# Eksik değerlerin doldurulması
data.ffill(inplace=True)

# Çıkıntıların (outliers) belirlenmesi ve yönetilmesi
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns

# Z-Score hesaplama
z_scores = np.abs(zscore(data[numeric_columns]))

# Z-Score > 3 olan verileri çıkıntı olarak belirleyelim ve kaldırılacak satırları işaretleyelim
data_cleaned = data[(z_scores < 3).all(axis=1)].copy()

print(f"Original data shape: {data.shape}")
print(f"Data shape after removing outliers: {data_cleaned.shape}")

# Sonuçları bir metin dosyasına yazdıralım (çıkıntıların belirlenmesi ve yönetilmesi)
with open('pokemon_outlier_removal_summary.txt', 'w', encoding='utf-8') as file:
    file.write("Original data shape:\n")
    file.write(str(data.shape))
    file.write("\n\nData shape after removing outliers:\n")
    file.write(str(data_cleaned.shape))

print("Outlier removal summary has been written to pokemon_outlier_removal_summary.txt")

# Numerik verilerin dönüştürülmesi
data_cleaned[numeric_columns] = data_cleaned[numeric_columns].astype('float64')

# Numerik verilerin ölçeklendirilmesi
scaler = StandardScaler()
data_cleaned.loc[:, numeric_columns] = scaler.fit_transform(data_cleaned[numeric_columns])

# Ölçeklendirilmiş verileri kontrol edelim
print(data_cleaned.head())

# Sonuçları bir metin dosyasına yazdıralım (ölçeklendirme)
with open('pokemon_feature_scaling_summary.txt', 'w', encoding='utf-8') as file:
    file.write("Head of the data after feature scaling:\n")
    file.write(data_cleaned.head().to_string())

print("Feature scaling summary has been written to pokemon_feature_scaling_summary.txt")
