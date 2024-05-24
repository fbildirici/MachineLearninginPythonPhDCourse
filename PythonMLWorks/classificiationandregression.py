import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, mean_squared_error, r2_score
from imblearn.over_sampling import SMOTE

# Veriyi yükleyelim
data = pd.read_csv(r'C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Homework\ML\pokemon.csv')

# Orijinal veri setindeki is_legendary dağılımını kontrol edelim
print("Original class distribution:")
print(data['is_legendary'].value_counts())

# Sütun adlarını kontrol edelim
print("Columns in dataset:", data.columns)

# Kategorik verileri sayısallaştırma (one-hot encoding)
if 'type1' in data.columns and 'type2' in data.columns:
    data = pd.get_dummies(data, columns=['type1', 'type2'], drop_first=True)
else:
    print("Specified columns are not in the dataset")

# Eksik değerlerin doldurulması
data.ffill(inplace=True)

# Sayısal olmayan sütunları kontrol edelim
non_numeric_columns = data.select_dtypes(include=['object']).columns
print("Non-numeric columns:", non_numeric_columns)

# Sayısal olmayan sütunları çıkaralım
data_cleaned = data.drop(columns=non_numeric_columns)

# Numerik verilerin ölçeklendirilmesi
numeric_columns = data_cleaned.select_dtypes(include=['float64', 'int64']).columns
scaler = StandardScaler()
data_cleaned.loc[:, numeric_columns] = scaler.fit_transform(data_cleaned[numeric_columns])

# Mevcut sütunları kontrol edelim
print("Columns in cleaned dataset:", data_cleaned.columns)

# Temizlenmiş veri setindeki is_legendary dağılımını kontrol edelim
print("Cleaned class distribution:")
print(data_cleaned['is_legendary'].value_counts())

# Sınıflandırma Modeli: Karar Ağacı
# Özellikler ve hedef değişken
X_class = data_cleaned.drop(columns=['is_legendary'])
y_class = data_cleaned['is_legendary']

# Veri dengesizliğini kontrol edelim
print("Class distribution before resampling:", y_class.value_counts())

# Sadece bir sınıf varsa hata mesajı verelim
if len(y_class.unique()) == 1:
    raise ValueError("The target 'y_class' needs to have more than 1 class. Got 1 class instead.")

# SMOTE kullanarak veri setini dengeli hale getirelim
smote = SMOTE(random_state=42)
X_class_res, y_class_res = smote.fit_resample(X_class, y_class)

# Veri dengesizliğini tekrar kontrol edelim
print("Class distribution after resampling:", y_class_res.value_counts())

# Eğitim ve test verisi
X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(X_class_res, y_class_res, test_size=0.3, random_state=42)

# Model oluşturma
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train_class, y_train_class)

# Tahminler
y_pred_class = clf.predict(X_test_class)

# Model değerlendirme
accuracy = accuracy_score(y_test_class, y_pred_class)
conf_matrix = confusion_matrix(y_test_class, y_pred_class)
class_report = classification_report(y_test_class, y_pred_class)

# Sonuçları yazdırma
with open('classification_results.txt', 'w', encoding='utf-8') as file:
    file.write("Accuracy:\n")
    file.write(str(accuracy))
    file.write("\n\nConfusion Matrix:\n")
    file.write(str(conf_matrix))
    file.write("\n\nClassification Report:\n")
    file.write(class_report)

print("Classification results have been written to classification_results.txt")

# Regresyon Modeli: Lineer Regresyon
# Özellikler ve hedef değişken
X_reg = data_cleaned.drop(columns=['attack'])
y_reg = data_cleaned['attack']

# Eğitim ve test verisi
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.3, random_state=42)

# Model oluşturma
reg = LinearRegression()
reg.fit(X_train_reg, y_train_reg)

# Tahminler
y_pred_reg = reg.predict(X_test_reg)

# Model değerlendirme
mse = mean_squared_error(y_test_reg, y_pred_reg)
r2 = r2_score(y_test_reg, y_pred_reg)

# Sonuçları yazdırma
with open('regression_results.txt', 'w', encoding='utf-8') as file:
    file.write("Mean Squared Error:\n")
    file.write(str(mse))
    file.write("\n\nR^2 Score:\n")
    file.write(str(r2))

print("Regression results have been written to regression_results.txt")
