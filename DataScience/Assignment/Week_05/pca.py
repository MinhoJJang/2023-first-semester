import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load the dataset into a pandas DataFrame
df = pd.read_csv('california_housing_train.csv')

# Fill in the missing values with the median value of each feature
df = df.fillna(df.median(numeric_only=True))

# Remove any unnecessary columns
df = df.drop(columns=['ocean_proximity'])

# Split the dataset into features and target variables
X = df.drop(columns=['median_house_value'])
y = df['median_house_value']

# Standardize the feature variables
scaler = StandardScaler()
X_std = scaler.fit_transform(X)

# Apply PCA to the standardized feature variables
pca = PCA()
X_pca = pca.fit_transform(X_std)

# Determine the number of principal components to keep
explained_var = pca.explained_variance_ratio_
cumulative_var = explained_var.cumsum()
n_components = 0
for i in range(len(cumulative_var)):
    if cumulative_var[i] >= 0.95:
        n_components = i + 1
        break

# Transform the standardized feature variables using PCA
pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X_std)

# Create a DataFrame with the reduced dataset
df_pca = pd.DataFrame(X_pca, columns=[f"PC{i+1}" for i in range(n_components)])
df_pca['median_house_value'] = y

import matplotlib.pyplot as plt

# Visualize the first two principal components
plt.scatter(df_pca['PC1'], df_pca['PC2'], c=df_pca['median_house_value'], cmap='viridis')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.colorbar(label='median_house_value')
plt.show()
