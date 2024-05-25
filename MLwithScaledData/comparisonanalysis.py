import pandas as pd

# Classification sonuçlarını okuma
classification_results_file = 'classificationfullof_results.txt'
with open(classification_results_file, 'r', encoding='utf-8') as f:
    classification_results = f.read()

# Regression sonuçlarını okuma
regression_results_file = 'regressionfullof_results.txt'
with open(regression_results_file, 'r', encoding='utf-8') as f:
    regression_results = f.read()

# Classification sonuçlarını ayıklama
classification_metrics = {}
lines = classification_results.split('\n')

# Hata ayıklama amacıyla dosyanın ilk birkaç satırını yazdırma
print("Classification results file content:")
for line in lines[:20]:  # İlk 20 satırı yazdır
    print(line)

# Ayrıştırma işlemi
for line in lines:
    if line.strip() == '':
        continue
    parts = line.split(":")
    if len(parts) == 2:
        key = parts[0].strip()
        try:
            value = float(parts[1].strip())
            classification_metrics[key] = value
        except ValueError:
            pass

# Regression sonuçlarını ayıklama
regression_metrics = {}
lines = regression_results.split('\n')

# Hata ayıklama amacıyla dosyanın ilk birkaç satırını yazdırma
print("\nRegression results file content:")
for line in lines[:20]:  # İlk 20 satırı yazdır
    print(line)

# Ayrıştırma işlemi
for line in lines:
    if line.strip() == '':
        continue
    parts = line.split(":")
    if len(parts) == 2:
        key = parts[0].strip()
        try:
            value = float(parts[1].strip())
            regression_metrics[key] = value
        except ValueError:
            pass

# Karşılaştırmalı analiz sonuçlarını birleştirme ve yazdırma
comparison_results = {
    'Classification': classification_metrics,
    'Regression': regression_metrics
}

comparison_output_file = 'comparison_analysis_results.txt'
with open(comparison_output_file, 'w', encoding='utf-8') as f:
    f.write("Classification Results:\n")
    for key, value in classification_metrics.items():
        f.write(f"{key}: {value}\n")
    f.write("\nRegression Results:\n")
    for key, value in regression_metrics.items():
        f.write(f"{key}: {value}\n")

print("Comparison analysis results saved to", comparison_output_file)

# Konsola da yazdıralım
print("\nClassification Results:")
for key, value in classification_metrics.items():
    print(f"{key}: {value}")
print("\nRegression Results:")
for key, value in regression_metrics.items():
    print(f"{key}: {value}")
