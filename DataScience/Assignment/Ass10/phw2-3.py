# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
df = pd.read_csv('knn_data.csv')

# Encode the target variable
le = LabelEncoder()
df['lang'] = le.fit_transform(df['lang'])

# Define the features and target
X = df[['longitude', 'latitude']]
y = df['lang']

# Create a KNN model
knn = KNeighborsClassifier()

# Evaluate the model using 5-fold cross-validation
scores = cross_val_score(knn, X, y, cv=5)
print(f"Base model CV accuracy: {scores.mean()} +/- {scores.std()}")

# Define hyperparameters for GridSearch
params = {'n_neighbors': range(1, 11), 'weights': ['uniform', 'distance'], 'metric': ['euclidean', 'manhattan']}

# Create GridSearchCV object
grid = GridSearchCV(knn, params, cv=5)

# Fit the data to GridSearchCV object
grid.fit(X, y)

# Print the best parameters and score
print("Best parameters from GridSearch: ", grid.best_params_)
print("Best score from GridSearch: ", grid.best_score_)

# Define hyperparameters for RandomizedSearch
params = {'n_neighbors': range(1, 11), 'weights': ['uniform', 'distance'], 'metric': ['euclidean', 'manhattan']}

# Create RandomizedSearchCV object
random = RandomizedSearchCV(knn, params, cv=5)

# Fit the data to RandomizedSearchCV object
random.fit(X, y)

# Print the best parameters and score
print("Best parameters from RandomizedSearch: ", random.best_params_)
print("Best score from RandomizedSearch: ", random.best_score_)
