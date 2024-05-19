import pandas as pd
import numpy as np

file_path = r"C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Presentation\pokemon.csv"

pokemon_df = pd.read_csv(file_path)

# Tanımlayıcı istatistikler hesaplama
descriptive_stats = pokemon_df.describe(include='all')

data_types = pokemon_df.dtypes

# Eksik değer hesapla
missing_values = pokemon_df.isnull().sum()

# unique value hesapla
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
