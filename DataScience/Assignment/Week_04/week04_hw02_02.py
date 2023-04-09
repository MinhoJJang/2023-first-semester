from sklearn.datasets import fetch_california_housing

california = fetch_california_housing()
X = california.data
y = california.target
feature_names = california.feature_names

import pandas as pd
from sklearn.ensemble import ExtraTreesRegressor
import matplotlib.pyplot as plt

# Load the California housing dataset
california = fetch_california_housing()
X = california.data
y = california.target
feature_names = california.feature_names

# Fit an Extra Trees Regressor model
model = ExtraTreesRegressor(n_estimators=100)
model.fit(X, y)

# Plot the feature importances
feat_importances = pd.Series(model.feature_importances_, index=feature_names)
fig, ax = plt.subplots(figsize=(9, 6))
feat_importances.nlargest(10).plot(kind='barh', ax=ax)
plt.show()
