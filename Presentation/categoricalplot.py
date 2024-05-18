import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Presentation\pokemon.csv"

# CSV dosyasını oku
pokemon_df = pd.read_csv(file_path)

# Kategorik değişkenler için sütun grafikler (Bar Plots)
categorical_columns = ['abilities', 'type1', 'type2']
for column in categorical_columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(y=pokemon_df[column], order=pokemon_df[column].value_counts().index)
    plt.title(f'Count Plot of {column}')
    plt.xlabel('Count')
    plt.ylabel(column)
    plt.grid(True)
    plt.show()
