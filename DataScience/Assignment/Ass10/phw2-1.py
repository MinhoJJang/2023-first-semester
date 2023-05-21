# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv('linear_regression_data.csv')

# Define the features and target
X = df['distance'].values.reshape(-1,1)
y = df['delivery time']

# Split the dataset into 4/5 for training and 1/5 for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True, stratify=None)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Calculate and print the mean squared error
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error (4/5 split): ", mse)

# Calculate and print the R^2 score
r2 = r2_score(y_test, predictions)
print("R^2 Score (4/5 split): ", r2)

# Split the dataset into 3/5 for training and 2/5 for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42, shuffle=True, stratify=None)

# Train the model again
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Calculate and print the mean squared error
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error (3/5 split): ", mse)

# Calculate and print the R^2 score
r2 = r2_score(y_test, predictions)
print("R^2 Score (3/5 split): ", r2)
