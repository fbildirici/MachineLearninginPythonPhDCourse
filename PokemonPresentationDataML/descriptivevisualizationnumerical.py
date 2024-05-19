import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Presentation\pokemon.csv"

pokemon_df = pd.read_csv(file_path)

numeric_columns = ['attack', 'base_egg_steps', 'base_total', 'height_m', 'weight_kg']
for column in numeric_columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(pokemon_df[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

for column in numeric_columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=pokemon_df[column])
    plt.title(f'Box Plot of {column}')
    plt.xlabel(column)
    plt.grid(True)
    plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x=pokemon_df['height_m'], y=pokemon_df['weight_kg'])
plt.title('Scatter Plot of Height vs. Weight')
plt.xlabel('Height (m)')
plt.ylabel('Weight (kg)')
plt.grid(True)
plt.show()
