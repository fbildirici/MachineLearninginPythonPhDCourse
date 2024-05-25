import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, precision_score, recall_score, f1_score, roc_auc_score, roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import label_binarize

# Veriyi yükleyelim
file_path = r'C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Homework\ML\final_pokemon.csv'
data = pd.read_csv(file_path)

# İlk birkaç satırı görüntüleyelim ve veri seti bilgilerini yazdıralım
print("Veri setinin ilk birkaç satırı:")
print(data.head())

print("\nVeri Seti Bilgileri:")
print(data.info())

# Hedef değişkeni kategorik yapmak için dönüştürme
data['is_legendary'] = data['is_legendary'].astype(int)

# Özellikler ve hedef değişken (sınıflandırma için)
X_class = data.drop(columns=['is_legendary'])
y_class = data['is_legendary']

# Eğitim ve test setlerine ayırma
X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(X_class, y_class, test_size=0.3, random_state=42)

# Modelleri tanımlama
models = {
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42),
    'SVM': SVC(probability=True, random_state=42)
}

evaluation_metrics = pd.DataFrame()

for model_name, model in models.items():
    model.fit(X_train_class, y_train_class)
    y_pred_class = model.predict(X_test_class)
    y_pred_proba = model.predict_proba(X_test_class)[:, 1]

    accuracy = accuracy_score(y_test_class, y_pred_class)
    precision = precision_score(y_test_class, y_pred_class, average='weighted')
    recall = recall_score(y_test_class, y_pred_class, average='weighted')
    f1 = f1_score(y_test_class, y_pred_class, average='weighted')
    auc_score = roc_auc_score(y_test_class, y_pred_proba)

    new_metrics = pd.DataFrame({
        'Model': [model_name],
        'Accuracy': [accuracy],
        'Precision': [precision],
        'Recall': [recall],
        'F1 Score': [f1],
        'AUC Score': [auc_score]
    })

    # Boş veya tümü NA sütunları hariç tutma
    if not new_metrics.empty and not new_metrics.isna().all(axis=1).any():
        evaluation_metrics = pd.concat([evaluation_metrics, new_metrics], ignore_index=True)

print(evaluation_metrics)

# Sonuçları görselleştirme
plt.figure(figsize=(12, 8))
sns.barplot(x='Model', y='Accuracy', data=evaluation_metrics)
plt.title('Model Karşılaştırması - Doğruluk')
plt.show()

plt.figure(figsize=(12, 8))
sns.barplot(x='Model', y='Precision', data=evaluation_metrics)
plt.title('Model Karşılaştırması - Kesinlik')
plt.show()

plt.figure(figsize=(12, 8))
sns.barplot(x='Model', y='Recall', data=evaluation_metrics)
plt.title('Model Karşılaştırması - Duyarlılık')
plt.show()

plt.figure(figsize=(12, 8))
sns.barplot(x='Model', y='F1 Score', data=evaluation_metrics)
plt.title('Model Karşılaştırması - F1 Skoru')
plt.show()

plt.figure(figsize=(12, 8))
sns.barplot(x='Model', y='AUC Score', data=evaluation_metrics)
plt.title('Model Karşılaştırması - AUC Skoru')
plt.show()
