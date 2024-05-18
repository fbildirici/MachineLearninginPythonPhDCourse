import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dosya yolunu belirtin
file_path = r"C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Presentation\pokemon.csv"

# CSV dosyasını oku
pokemon_df = pd.read_csv(file_path)

# Scatter plot oluşturma (örneğin: attack ve defense arasındaki ilişki)
plt.figure(figsize=(10, 6))
sns.scatterplot(x=pokemon_df['attack'], y=pokemon_df['defense'])
plt.title('Scatter Plot of Attack vs. Defense')
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.grid(True)
plt.show()

# Scatter plot oluşturma (örneğin: height_m ve weight_kg arasındaki ilişki)
plt.figure(figsize=(10, 6))
sns.scatterplot(x=pokemon_df['height_m'], y=pokemon_df['weight_kg'])
plt.title('Scatter Plot of Height vs. Weight')
plt.xlabel('Height (m)')
plt.ylabel('Weight (kg)')
plt.grid(True)
plt.show()
