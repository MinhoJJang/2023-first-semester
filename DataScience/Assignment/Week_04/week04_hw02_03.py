import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

# Download the California housing dataset
california = fetch_california_housing()
X = california.data
y = california.target
feature_names = california.feature_names

# Plot correlation matrix heatmap
data = pd.DataFrame(X, columns=feature_names)
data["target"] = y
corrmat = data.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(9, 8))
sns.heatmap(data[top_corr_features].corr(), annot=True, cmap="RdYlGn")
plt.show()
