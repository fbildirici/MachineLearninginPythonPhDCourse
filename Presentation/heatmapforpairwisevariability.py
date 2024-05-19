import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dosya yolunu belirtin
file_path = r"C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Presentation\pokemon.csv"

# CSV dosyasını oku
pokemon_df = pd.read_csv(file_path)

# Sadece sayısal sütunları seç
numeric_df = pokemon_df.select_dtypes(include=[float, int])

# Korelasyon matrisi hesapla
correlation_matrix = numeric_df.corr()

# Heatmap oluşturma
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.show()
