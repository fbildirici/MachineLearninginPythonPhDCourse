import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Veriyi yükleyelim
file_path = r'C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Homework\ML\final_pokemon.csv'
data = pd.read_csv(file_path)

# Hedef değişkeni kategorik yapmak için dönüştürme (önceki koddan)
data['is_legendary'] = data['is_legendary'].astype(int)

# Özellikler ve hedef değişken (regresyon için)
X_reg = data.drop(columns=['attack'])
y_reg = data['attack']

# Eğitim ve test setlerine ayırma
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.3, random_state=42)

# Model oluşturma ve eğitme
reg = LinearRegression()
reg.fit(X_train_reg, y_train_reg)

# Tahminler
y_pred_reg = reg.predict(X_test_reg)

# Model değerlendirme
mse = mean_squared_error(y_test_reg, y_pred_reg)
r2 = r2_score(y_test_reg, y_pred_reg)

# Sonuçları dosyaya kaydedelim
regression_output_file = 'regression_results.txt'
with open(regression_output_file, 'w', encoding='utf-8') as f:
    f.write("Regression Mean Squared Error:\n")
    f.write(str(mse) + "\n\n")
    f.write("Regression R^2 Score:\n")
    f.write(str(r2) + "\n")

# Konsola da yazdıralım
print("Regression Mean Squared Error:", mse)
print("Regression R^2 Score:", r2)
