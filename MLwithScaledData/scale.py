import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification

# Load the dataset
file_path = r'C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Homework\ML\pokemon.csv'
data = pd.read_csv(file_path)

# Display the first few rows
print("First few rows of the dataset:")
print(data.head())

# Display dataset information
print("\nDataset Information:")
print(data.info())

# Handling missing values
print("\nHandling missing values...")
data.ffill(inplace=True)

# Remove non-numeric columns
print("\nRemoving non-numeric columns...")
non_numeric_columns = data.select_dtypes(include=['object']).columns
print("Non-numeric columns to be removed:", non_numeric_columns)
data_cleaned = data.drop(columns=non_numeric_columns)

# Scale numeric columns
print("\nScaling numeric columns...")
numeric_columns = data_cleaned.select_dtypes(include=['float64', 'int64']).columns
scaler = StandardScaler()
data_cleaned[numeric_columns] = scaler.fit_transform(data_cleaned[numeric_columns])

# Adding synthetic data for better balance and variety
print("\nAdding synthetic data...")
X_synthetic, y_synthetic = make_classification(n_samples=500, n_features=len(numeric_columns),
                                               n_informative=10, n_redundant=5, n_clusters_per_class=2,
                                               weights=[0.7, 0.3], flip_y=0.01, random_state=42)

# Convert synthetic data to DataFrame
synthetic_data = pd.DataFrame(X_synthetic, columns=numeric_columns)
synthetic_data['is_legendary'] = y_synthetic

# Combine original and synthetic data
final_data = pd.concat([data_cleaned, synthetic_data], ignore_index=True)

# Save the final dataset to a new CSV file
output_file_path = r'C:\Users\Fatih Bildirici\OneDrive\Documents\Desktop\Git Depoları\PhdCoursesAI\PhDCoursesAI\MachineLearningwithPython\Homework\ML\final_pokemon.csv'
final_data.to_csv(output_file_path, index=False)
print(f"\nFinal dataset saved to {output_file_path}")

# Display the final dataset information
print("\nFinal Dataset Information:")
print(final_data.info())

# Display the first few rows of the final dataset
print("\nFirst few rows of the final dataset:")
print(final_data.head())
