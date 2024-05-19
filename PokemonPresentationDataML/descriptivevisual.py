import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

file_path = r"C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Presentation\pokemon.csv"

pokemon_df = pd.read_csv(file_path)

# Descriptive istatistikler hesaplama
descriptive_stats = pokemon_df.describe(include='all')

# Veri tipleri
data_types = pokemon_df.dtypes

missing_values = pokemon_df.isnull().sum()

unique_values = pokemon_df.nunique()

numeric_columns = pokemon_df.select_dtypes(include=[np.number]).columns
extra_stats = pd.DataFrame(index=numeric_columns)
extra_stats['Range'] = pokemon_df[numeric_columns].max() - pokemon_df[numeric_columns].min()
extra_stats['Variance'] = pokemon_df[numeric_columns].var()
extra_stats['Skewness'] = pokemon_df[numeric_columns].skew()
extra_stats['Kurtosis'] = pokemon_df[numeric_columns].kurtosis()
extra_stats['Median'] = pokemon_df[numeric_columns].median()

summary_stats = pd.DataFrame({
    'Data Type': data_types,
    'Missing Values': missing_values,
    'Unique Values': unique_values
})

summary_stats = summary_stats.join(descriptive_stats.transpose())
summary_stats = summary_stats.join(extra_stats)

print(summary_stats)

output_path = r"C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Presentation\summary_statistics.xlsx"
summary_stats.to_excel(output_path, index=True)

print(f"Summary statistics saved to {output_path}")

# Görselleştirme

sns.pairplot(pokemon_df[numeric_columns])
plt.suptitle('Pair Plot of Numeric Features', y=1.02)
plt.show()

for column in numeric_columns:
    plt.figure(figsize=(14, 6))

    # Histogram ve KDE
    plt.subplot(1, 2, 1)
    sns.histplot(pokemon_df[column], kde=True, bins=30)
    plt.title(f'Histogram and KDE of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')

    # Boxplot
    plt.subplot(1, 2, 2)
    sns.boxplot(x=pokemon_df[column])
    plt.title(f'Boxplot of {column}')
    plt.xlabel(column)

    plt.tight_layout()
    plt.show()
