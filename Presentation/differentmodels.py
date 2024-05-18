import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, \
    classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Dosya yolunu belirtin
file_path = r"C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Presentation\pokemon.csv"

# CSV dosyasını oku
pokemon_df = pd.read_csv(file_path)

# Hedef değişkeni ve özellikleri belirleme
target = 'is_legendary'
features = ['attack', 'defense', 'sp_attack', 'sp_defense', 'speed', 'hp', 'height_m', 'weight_kg']

X = pokemon_df[features]
y = pokemon_df[target]

# Eksik değerleri kontrol etme
print(X.isnull().sum())

# Eksik değerleri doldurma
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Veriyi eğitime ve teste ayırma
X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.2, random_state=42)

# Veriyi ölçeklendirme
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model kurma ve eğitim
models = {
    'Logistic Regression': LogisticRegression(),
    'KNN': KNeighborsClassifier(),
    'Random Forest': RandomForestClassifier(),
    'Kernel SVM': SVC(kernel='rbf'),
    'Naive Bayes': GaussianNB(),
    'Decision Tree': DecisionTreeClassifier()
}

# Modelleri eğitme ve değerlendirme
results = {}

for model_name, model in models.items():
    # Modeli eğitme
    model.fit(X_train_scaled, y_train)

    # Tahmin yapma
    y_pred = model.predict(X_test_scaled)

    # Performans metriklerini hesaplama
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)

    # Cross-Validation Score
    cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
    cv_mean = np.mean(cv_scores)

    results[model_name] = {
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall,
        'F1 Score': f1,
        'Confusion Matrix': conf_matrix,
        'Classification Report': class_report,
        'Cross-Validation Mean': cv_mean
    }

# Sonuçları yazdırma ve dışa aktarma
output_file_path = r"C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Presentation\model_results.txt"
with open(output_file_path, 'w') as file:
    for model_name, metrics in results.items():
        file.write(f"Model: {model_name}\n")
        file.write(f"Accuracy: {metrics['Accuracy']:.4f}\n")
        file.write(f"Precision: {metrics['Precision']:.4f}\n")
        file.write(f"Recall: {metrics['Recall']:.4f}\n")
        file.write(f"F1 Score: {metrics['F1 Score']:.4f}\n")
        file.write(f"Cross-Validation Mean: {metrics['Cross-Validation Mean']:.4f}\n")
        file.write("Confusion Matrix:\n")
        file.write(np.array2string(metrics['Confusion Matrix']))
        file.write("\n")
        file.write("Classification Report:\n")
        file.write(metrics['Classification Report'])
        file.write("\n\n")

print(f"Results exported to {output_file_path}")

# Confusion matrix'leri görselleştirme
for model_name, metrics in results.items():
    plt.figure(figsize=(6, 4))
    sns.heatmap(metrics['Confusion Matrix'], annot=True, fmt='d', cmap='Blues')
    plt.title(f'Confusion Matrix: {model_name}')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()
