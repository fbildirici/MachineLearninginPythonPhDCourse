import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, precision_score, recall_score, \
    f1_score, roc_auc_score, roc_curve, auc
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

# Her model için değerlendirme metriklerini depolamak için boş bir DataFrame oluşturma
evaluation_metrics = pd.DataFrame(columns=['Model', 'Accuracy', 'Precision', 'Recall', 'F1 Score', 'AUC Score'])

# Modelleri eğitme ve değerlendirme
for model_name, model in models.items():
    model.fit(X_train_class, y_train_class)
    y_pred_class = model.predict(X_test_class)
    y_pred_proba = model.predict_proba(X_test_class)

    accuracy = accuracy_score(y_test_class, y_pred_class)
    precision = precision_score(y_test_class, y_pred_class, average='weighted')
    recall = recall_score(y_test_class, y_pred_class, average='weighted')
    f1 = f1_score(y_test_class, y_pred_class, average='weighted')
    auc_score = roc_auc_score(y_test_class, y_pred_proba, multi_class='ovr')

    new_metrics = pd.DataFrame({
        'Model': [model_name],
        'Accuracy': [accuracy],
        'Precision': [precision],
        'Recall': [recall],
        'F1 Score': [f1],
        'AUC Score': [auc_score]
    })

    # Concat new metrics if not empty or all-NA
    if not new_metrics.empty and not new_metrics.isna().all(axis=None):
        evaluation_metrics = pd.concat([evaluation_metrics, new_metrics], ignore_index=True)

    # Confusion Matrix Görselleştirme
    conf_matrix = confusion_matrix(y_test_class, y_pred_class)
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Not Legendary', 'Legendary'],
                yticklabels=['Not Legendary', 'Legendary'])
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title(f'{model_name} - Confusion Matrix')
    plt.show()

    # ROC Eğrisi için One-vs-Rest (OvR) yaklaşımı
    y_test_binarized = label_binarize(y_test_class, classes=[0, 1])
    n_classes = y_test_binarized.shape[1]

    # Her sınıf için ROC eğrisi ve AUC
    fpr = dict()
    tpr = dict()
    roc_auc = dict()

    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(y_test_binarized[:, i], y_pred_proba[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    # ROC Eğrisini Çizme
    plt.figure(figsize=(8, 6))
    for i in range(n_classes):
        plt.plot(fpr[i], tpr[i], lw=2, label=f'Class {i} ROC curve (area = {roc_auc[i]:.2f})')
    plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'{model_name} - Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc="lower right")
    plt.show()

# Model Performansı Metriklerini Görselleştirme
plt.figure(figsize=(12, 8))
metrics_to_plot = ['Accuracy', 'Precision', 'Recall', 'F1 Score', 'AUC Score']
for metric in metrics_to_plot:
    plt.plot(evaluation_metrics['Model'], evaluation_metrics[metric], label=metric, marker='o')
plt.title('Model Performance Metrics Comparison')
plt.xlabel('Models')
plt.ylabel('Scores')
plt.ylim(0, 1)
plt.legend(loc='lower right')
plt.show()

# Sonuçları dosyaya kaydedelim
classification_output_file = 'differenttrial.txt'
with open(classification_output_file, 'w', encoding='utf-8') as f:
    for idx, row in evaluation_metrics.iterrows():
        f.write(f"{row['Model']}:\n")
        f.write(f"Accuracy: {row['Accuracy']}\n")
        f.write(f"Precision: {row['Precision']}\n")
        f.write(f"Recall: {row['Recall']}\n")
        f.write(f"F1 Score: {row['F1 Score']}\n")
        f.write(f"AUC Score: {row['AUC Score']}\n")
        f.write("\n")

# Konsola da yazdıralım
print(evaluation_metrics)
