import pandas as pd
from sklearn.decomposition import PCA

# Load the data
data = pd.read_csv('california_housing_train.csv')

# Separate the features and target variable
X = data.drop('median_house_value', axis=1)
y = data['median_house_value']

# Perform PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# The transformed data is now stored in X_pca

import matplotlib.pyplot as plt

# Plot the transformed data
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.show()