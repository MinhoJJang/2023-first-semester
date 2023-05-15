

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set print options for NumPy
np.set_printoptions(suppress=True, precision=2)

# Set the dataset from Exercise 1
data = pd.DataFrame({
    'Person': [1, 2, 3, 4, 5],
    'Age': [30, 40, 50, 60, 30],
    'Income': [200, 300, 800, 600, 300],
    'Yrs worked': [10, 20, 20, 20, 20],
    'Vacation': [4, 4, 1, 2, 5]
})

# Drop 'Person' column as it's not a numeric variable
data_numeric = data.drop('Person', axis=1)

# Calculate the population covariance matrix
pop_cov_matrix = np.cov(data_numeric.T, bias=True)

# Calculate the sample covariance matrix
sample_cov_matrix = np.cov(data_numeric.T, bias=False)

# Print population covariance matrix
print("Population Covariance Matrix:")
print(pop_cov_matrix)

# Print sample covariance matrix
print("\nSample Covariance Matrix:")
print(sample_cov_matrix)

# Visualize the covariance matrix using Seaborn
plt.figure(figsize=(10, 6))
sns.heatmap(pop_cov_matrix, annot=True, cmap="coolwarm", xticklabels=data_numeric.columns, yticklabels=data_numeric.columns)
plt.title("Population Covariance Matrix Heatmap")
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(sample_cov_matrix, annot=True, cmap="coolwarm", xticklabels=data_numeric.columns, yticklabels=data_numeric.columns)
plt.title("Sample Covariance Matrix Heatmap")
plt.show()
