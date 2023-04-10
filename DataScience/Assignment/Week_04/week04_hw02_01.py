from sklearn.datasets import fetch_california_housing
from sklearn.feature_selection import SelectKBest, f_regression
import pandas as pd

# 해당 사이트 참고 https://inria.github.io/scikit-learn-mooc/python_scripts/datasets_california_housing.html

# Download the California housing dataset
california = fetch_california_housing()
X = california.data
y = california.target
feature_names = california.feature_names

# Apply SelectKBest class to extract best features
selector = SelectKBest(f_regression, k='all')
selector.fit(X, y)

# Create dataframe of scores and feature names
dfscores = pd.DataFrame(selector.scores_, columns=["Score"])
dfcolumns = pd.DataFrame(feature_names, columns=["Feature"])
featureScores = pd.concat([dfcolumns,dfscores],axis=1)

# Sort features by score in descending order
sorted_features = featureScores.nlargest(10, "Score")

# Print the 10 best features
print("Best Features selected by SelectKBest:")
print(sorted_features)

