import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, precision_score, recall_score, f1_score, roc_auc_score

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

# Model oluşturma ve eğitme
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train_class, y_train_class)

# Tahminler
y_pred_class = clf.predict(X_test_class)
y_pred_proba = clf.predict_proba(X_test_class)

# Model değerlendirme
accuracy = accuracy_score(y_test_class, y_pred_class)
precision = precision_score(y_test_class, y_pred_class, average='weighted')
recall = recall_score(y_test_class, y_pred_class, average='weighted')
f1 = f1_score(y_test_class, y_pred_class, average='weighted')
conf_matrix = confusion_matrix(y_test_class, y_pred_class)
class_report = classification_report(y_test_class, y_pred_class)
auc = roc_auc_score(y_test_class, y_pred_proba, multi_class='ovr')

# Sonuçları dosyaya kaydedelim
classification_output_file = 'classificationfullof_results.txt'
with open(classification_output_file, 'w', encoding='utf-8') as f:
    f.write("Classification Accuracy:\n")
    f.write(str(accuracy) + "\n\n")
    f.write("Precision:\n")
    f.write(str(precision) + "\n\n")
    f.write("Recall:\n")
    f.write(str(recall) + "\n\n")
    f.write("F1 Score:\n")
    f.write(str(f1) + "\n\n")
    f.write("Confusion Matrix:\n")
    f.write(str(conf_matrix) + "\n\n")
    f.write("Classification Report:\n")
    f.write(class_report + "\n")
    f.write("AUC Score:\n")
    f.write(str(auc) + "\n")

# Konsola da yazdıralım
print("Classification Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)
print("AUC Score:", auc)
