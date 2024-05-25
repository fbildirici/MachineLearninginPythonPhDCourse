import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns

# Veriyi yükleyelim
file_path = r'C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Homework\ML\final_pokemon.csv'
data = pd.read_csv(file_path)

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
mae = mean_absolute_error(y_test_reg, y_pred_reg)
r2 = r2_score(y_test_reg, y_pred_reg)

# Gerçek vs Tahmin Grafiği
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test_reg, y=y_pred_reg, edgecolor='w', alpha=0.7)
plt.plot([y_test_reg.min(), y_test_reg.max()], [y_test_reg.min(), y_test_reg.max()], color='red', lw=2)
plt.xlabel('Actual Attack')
plt.ylabel('Predicted Attack')
plt.title('Actual vs Predicted Attack')
plt.show()

# Sonuçları dosyaya kaydedelim
regression_output_file = 'regressionfullof_results.txt'
with open(regression_output_file, 'w', encoding='utf-8') as f:
    f.write("Regression Mean Squared Error (MSE):\n")
    f.write(str(mse) + "\n\n")
    f.write("Regression Mean Absolute Error (MAE):\n")
    f.write(str(mae) + "\n\n")
    f.write("Regression R^2 Score:\n")
    f.write(str(r2) + "\n")

# Konsola da yazdıralım
print("Regression Mean Squared Error (MSE):", mse)
print("Regression Mean Absolute Error (MAE):", mae)
print("Regression R^2 Score:", r2)
