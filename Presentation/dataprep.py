import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Dosya yolunu belirtin
file_path = r"C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Presentation\pokemon.csv"

# CSV dosyasını oku
pokemon_df = pd.read_csv(file_path)

# Hedef değişkeni ve özellikleri belirleme
target = 'is_legendary'
features = ['attack', 'defense', 'sp_attack', 'sp_defense', 'speed', 'hp', 'height_m', 'weight_kg']

X = pokemon_df[features]
y = pokemon_df[target]

# Veriyi eğitime ve teste ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Veriyi ölçeklendirme
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# İlk birkaç satırı kontrol etme
print(X_train_scaled[:5])
print(X_test_scaled[:5])
print(y_train[:5])
print(y_test[:5])
