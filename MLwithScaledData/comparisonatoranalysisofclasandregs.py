import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression, LinearRegression, Ridge
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, roc_curve, auc, confusion_matrix
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import label_binarize

# Veriyi yükleyelim
file_path = r'C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Homework\ML\final_pokemon.csv'
data = pd.read_csv(file_path)

# Classification Analizi
data['is_legendary'] = data['is_legendary'].astype(int)

X_class = data.drop(columns=['is_legendary'])
y_class = data['is_legendary']

X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(X_class, y_class, test_size=0.3, random_state=42)

classification_models = {
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42),
    'SVM': SVC(probability=True, random_state=42)
}

classification_metrics = pd.DataFrame(columns=['Model', 'Accuracy', 'Precision', 'Recall', 'F1 Score', 'AUC Score'])

for model_name, model in classification_models.items():
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

    if not new_metrics.empty and not new_metrics.isna().all(axis=None):
        classification_metrics = pd.concat([classification_metrics, new_metrics], ignore_index=True)

    # Confusion Matrix Visualization
    conf_matrix = confusion_matrix(y_test_class, y_pred_class)
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Not Legendary', 'Legendary'],
                yticklabels=['Not Legendary', 'Legendary'])
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title(f'{model_name} - Confusion Matrix')
    plt.show()

    # ROC Curve for One-vs-Rest (OvR) approach
    y_test_binarized = label_binarize(y_test_class, classes=[0, 1])
    n_classes = y_test_binarized.shape[1]

    fpr = dict()
    tpr = dict()
    roc_auc = dict()

    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(y_test_binarized[:, i], y_pred_proba[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    plt.figure(figsize=(8, 6))
    for i in range(n_classes):
        plt.plot(fpr[i], tpr[i], lw=2, label=f'Class {i} ROC curve (area = {roc_auc[i]:.2f})')
    plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'{model_name} - Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc="lower right")
    plt.show()

# Regression Analizi
X_reg = data.drop(columns=['attack'])
y_reg = data['attack']

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.3, random_state=42)

regression_models = {
    'Linear Regression': LinearRegression(),
    'Ridge Regression': Ridge(alpha=1.0),
    'Random Forest Regressor': RandomForestRegressor(random_state=42)
}

regression_metrics = pd.DataFrame(columns=['Model', 'MSE', 'MAE', 'R^2 Score'])

for model_name, model in regression_models.items():
    model.fit(X_train_reg, y_train_reg)
    y_pred_reg = model.predict(X_test_reg)

    mse = mean_squared_error(y_test_reg, y_pred_reg)
    mae = mean_absolute_error(y_test_reg, y_pred_reg)
    r2 = r2_score(y_test_reg, y_pred_reg)

    new_metrics = pd.DataFrame({
        'Model': [model_name],
        'MSE': [mse],
        'MAE': [mae],
        'R^2 Score': [r2]
    })

    if not new_metrics.empty and not new_metrics.isna().all(axis=None):
        regression_metrics = pd.concat([regression_metrics, new_metrics], ignore_index=True)

    # Actual vs Predicted Scatter Plot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=y_test_reg, y=y_pred_reg, edgecolor='w', alpha=0.7)
    plt.plot([y_test_reg.min(), y_test_reg.max()], [y_test_reg.min(), y_test_reg.max()], color='red', lw=2)
    plt.xlabel('Actual Attack')
    plt.ylabel('Predicted Attack')
    plt.title(f'Actual vs Predicted Attack ({model_name}) - Scatter Plot')
    plt.show()

    # Actual vs Predicted Line Plot
    plt.figure(figsize=(8, 6))
    plt.plot(y_test_reg.values, label='Actual')
    plt.plot(y_pred_reg, label='Predicted', linestyle='--')
    plt.xlabel('Sample')
    plt.ylabel('Attack')
    plt.title(f'Actual vs Predicted Attack ({model_name}) - Line Plot')
    plt.legend()
    plt.show()

# Classification and Regression Performance Comparison
print("Classification Metrics:")
print(classification_metrics)
print("\nRegression Metrics:")
print(regression_metrics)

# Save results to files
classification_output_file = 'classification_endgame.txt'
with open(classification_output_file, 'w', encoding='utf-8') as f:
    classification_metrics.to_string(f)

regression_output_file = 'regression_endgame.txt'
with open(regression_output_file, 'w', encoding='utf-8') as f:
    regression_metrics.to_string(f)

# Classification Model Performance Metrics Visualization
plt.figure(figsize=(12, 8))
metrics_to_plot = ['Accuracy', 'Precision', 'Recall', 'F1 Score', 'AUC Score']
for metric in metrics_to_plot:
    plt.plot(classification_metrics['Model'], classification_metrics[metric], label=metric, marker='o')
plt.title('Classification Model Performance Metrics Comparison')
plt.xlabel('Models')
plt.ylabel('Scores')
plt.ylim(0, 1)
plt.legend(loc='lower right')
plt.show()

# Regression Model Performance Metrics Visualization (Line Plot)
plt.figure(figsize=(12, 8))
plt.plot(regression_metrics['Model'], regression_metrics['MSE'], marker='o', label='MSE')
plt.plot(regression_metrics['Model'], regression_metrics['MAE'], marker='o', label='MAE')
plt.plot(regression_metrics['Model'], regression_metrics['R^2 Score'], marker='o', label='R^2 Score')
plt.title('Regression Model Performance Metrics Comparison')
plt.xlabel('Models')
plt.ylabel('Scores')
plt.legend(loc='upper right')
plt.show()
